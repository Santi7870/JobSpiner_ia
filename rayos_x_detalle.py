from playwright.sync_api import sync_playwright

def escanear_detalle_oferta():
    with sync_playwright() as p:
        print("🩻 Escaneando página de detalle...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Usamos una URL real que encontramos en tu prueba anterior
        url_prueba = "https://weworkremotely.com/remote-jobs/onthegosystems-php-developer-french-or-german-speakers"
        
        print(f"🌍 Entrando a: {url_prueba}")
        page.goto(url_prueba)
        
        # Esperamos un poco a que cargue
        page.wait_for_timeout(3000)

        # ESTRATEGIA: Vamos a buscar el contenedor principal.
        # En WWR suele llamarse "job-listing-content" o "listing-container".
        # Vamos a intentar imprimir el HTML de esa zona.
        
        print("🔍 Buscando el texto de la oferta...")
        
        # Intentamos buscar por el ID común en este sitio
        contenido = page.query_selector("#job-listing-content")
        
        if contenido:
            print("\n✅ ¡LO ENCONTRÉ! Aquí está el inicio del texto:\n")
            texto_limpio = contenido.inner_text()
            print("------------------------------------------------")
            print(texto_limpio[:500]) # Solo imprimimos los primeros 500 caracteres
            print("------------------------------------------------")
            print("\n(Si lees texto legible arriba, ya tenemos el selector correcto)")
        else:
            print("❌ No encontré el contenedor con ID '#job-listing-content'. Hay que buscar otro.")

        browser.close()

if __name__ == "__main__":
    escanear_detalle_oferta()