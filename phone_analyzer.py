import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser


# ----------------------------------------
# Configuration : Ajouter votre clé OpenCage
# ----------------------------------------
OPENCAGE_KEY = "YOUR_OPENCAGE_API_KEY"


def analyze_number(phone_number):
    """
    Analyse un numéro de téléphone pour en extraire les informations :
    pays, région, opérateur, fuseaux horaires et localisation géographique.
    Retourne un dictionnaire avec les résultats.
    """
    try:
        # Parsing du numéro de téléphone
        parsed_number = phonenumbers.parse(phone_number)

        # Pays et région
        country = geocoder.country_name_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "en")

        # Opérateur télécom
        service_provider = carrier.name_for_number(parsed_number, "en")

        # Fuseau horaire
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Géocodage via OpenCage
        geocoder_oc = OpenCageGeocode(OPENCAGE_KEY)
        results = geocoder_oc.geocode(region)

        if results and len(results):
            lat = results[0]['geometry']['lat']
            lng = results[0]['geometry']['lng']
        else:
            lat = lng = None

        return {
            "country": country,
            "region": region,
            "carrier": service_provider,
            "time_zones": time_zones,
            "latitude": lat,
            "longitude": lng
        }

    except Exception as e:
        return {"error": str(e)}


def show_result():
    """
    Action exécutée lors du clic sur le bouton "Analyser".
    Affiche les résultats de l’analyse et génère une carte si possible.
    """
    phone_number = entry_number.get()
    if not phone_number:
        messagebox.showerror("Erreur", "Veuillez entrer un numéro de téléphone.")
        return

    result = analyze_number(phone_number)

    if "error" in result:
        messagebox.showerror("Erreur", result["error"])
        return

    # Construction du texte affiché
    output_text = (
        f"📌 Country : {result['country']}\n"
        f"📍 Region : {result['region']}\n"
        f"📡 Carrier : {result['carrier']}\n"
        f"⏰ Timezone(s) : {result['time_zones']}\n"
    )

    if result["latitude"] and result["longitude"]:
        output_text += f"🌍 Latitude : {result['latitude']}, Longitude : {result['longitude']}\n"

        # Création d’une carte avec Folium
        my_map = folium.Map(location=[result["latitude"], result["longitude"]], zoom_start=9)
        folium.Marker([result["latitude"], result["longitude"]], popup=result["region"]).add_to(my_map)
        my_map.save("phone_location.html")

        output_text += "\n✅ Carte générée : phone_location.html"
        webbrowser.open("phone_location.html")

    else:
        output_text += "\n❌ Localisation géographique indisponible."

    # Affichage dans la zone de sortie
    text_result.config(state=tk.NORMAL)
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, output_text)
    text_result.config(state=tk.DISABLED)


# ----------------------------------------
# Interface graphique Tkinter
# ----------------------------------------
root = tk.Tk()
root.title("Analyseur de Numéro Téléphonique")
root.geometry("600x400")
root.resizable(False, False)

# Label et champ de saisie
label_number = tk.Label(root, text="Entrez un numéro avec indicatif (ex: +14155552671) :", font=("Arial", 12))
label_number.pack(pady=10)

entry_number = tk.Entry(root, width=40, font=("Arial", 12))
entry_number.pack(pady=5)

# Bouton d’exécution
btn_analyze = tk.Button(root, text="🔍 Analyser", command=show_result, font=("Arial", 12), bg="#4CAF50", fg="white")
btn_analyze.pack(pady=10)

# Zone d’affichage des résultats
text_result = tk.Text(root, height=12, width=70, state=tk.DISABLED, font=("Arial", 11))
text_result.pack(pady=10)

root.mainloop()
