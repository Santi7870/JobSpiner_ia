from playwright.sync_api import sync_playwright

def buscar_trabajos_reales():
    with sync_playwright() as p:
        print("🚀 Lanzando JobSniper (Modo Precisión)...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        url = "https://weworkremotely.com/categories/remote-back-end-programming-jobs"
        print(f"🌍 Scrapeando: {url}")
        page.goto(url)
        
        # Esperamos a la lista
        page.wait_for_selector("section.jobs", timeout=10000)

        # Seleccionamos TODAS las filas de la lista
        filas = page.query_selector_all("section.jobs li")
        
        resultados = []
        print(f"👀 Analizando {len(filas)} filas encontradas...")

        for fila in filas:
            # 1. Buscamos el link principal que envuelve la oferta
            # Usamos la clase que vimos en tu HTML: "listing-link--unlocked"
            # Ojo: A veces hay filas que no son links (headers), esas darán None y las saltamos.
            elemento_link = fila.query_selector("a[href*='/remote-jobs/']")
            
            if elemento_link:
                # --- AQUÍ APUNTAMOS CON PRECISIÓN ---
                
                # Buscar Título (h3 con clase específica)
                el_titulo = elemento_link.query_selector("h3.new-listing__header__title")
                titulo = el_titulo.inner_text().strip() if el_titulo else "Sin título"
                
                # Buscar Empresa (p con clase específica)
                el_empresa = elemento_link.query_selector("p.new-listing__company-name")
                empresa = el_empresa.inner_text().strip() if el_empresa else "Empresa oculta"
                
                # Sacar Link
                url_parcial = elemento_link.get_attribute("href")
                url_completa = "https://weworkremotely.com" + url_parcial
                
                print(f"✅ Oferta: {titulo} | 🏢 {empresa}")
                
                resultados.append({
                    "puesto": titulo,
                    "empresa": empresa,
                    "url": url_completa
                })
        
        print(f"\n🎉 Misión Cumplida: {len(resultados)} ofertas capturadas.")
        browser.close()
        return resultados

if __name__ == "__main__":
    buscar_trabajos_reales()