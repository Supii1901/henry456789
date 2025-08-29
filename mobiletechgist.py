# import streamlit as st
# import requests
# import datetime
# import pandas as pd

# # ----------------------------
# # Page config
# # ----------------------------
# st.set_page_config(page_title="Mobile Tech Gist", layout="wide", page_icon="📱")

# # ----------------------------
# # Exchange rate (cached)
# # ----------------------------
# @st.cache_data(ttl=3600)
# def fetch_usd_to_ngn():
#     """Fetch USD -> NGN (no API key). Returns (rate, last_update_str)."""
#     try:
#         # exchangerate.host is free and requires no API key
#         r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=NGN", timeout=8)
#         data = r.json()
#         rate = data.get("rates", {}).get("NGN")
#         ts = data.get("timestamp") or data.get("date")
#         if rate is None:
#             raise ValueError("No rate")
#         if isinstance(ts, int):
#             last = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             last = str(ts)
#         return float(rate), last
#     except Exception:
#         # fallback conservative default
#         return 1600.0, "Unavailable (fallback)"

# def convert_usd_to_ngn_str(price_usd_str, rate):
#     try:
#         val = float(price_usd_str.replace("$", "").replace(",", "").strip())
#         ngn = val * rate
#         return f"₦{ngn:,.0f}"
#     except Exception:
#         return "₦---"

# def price_usd_with_commas(price_str):
#     try:
#         v = float(price_str.replace("$","").replace(",",""))
#         return f"${v:,.0f}"
#     except:
#         return price_str

# # manual refresh button in sidebar
# if st.sidebar.button("🔄 Refresh exchange rate"):
#     st.cache_data.clear()

# usd_to_ngn_rate, rate_last_updated = fetch_usd_to_ngn()

# # ----------------------------
# # Backgrounds (real gadget showcase; dimmed)
# # hosted online (darkened by query params where possible)
# # ----------------------------
# backgrounds = {
#     "Home": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1600&auto=format&fit=crop&sat=-30",
#     "Devices": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1600&auto=format&fit=crop&sat=-30",
#     "Compare": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=1600&auto=format&fit=crop&sat=-30",
#     "About": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1600&auto=format&fit=crop&sat=-30",
# }

# def apply_background(page_key):
#     url = backgrounds.get(page_key)
#     if not url:
#         return
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("{url}");
#             background-size: cover;
#             background-position: center;
#             background-attachment: fixed;
#             color: #e6eef8;
#         }}
#         /* translucent card for readable content */
#         .mtg-card {{
#             background: linear-gradient(rgba(4,8,16,0.78), rgba(4,8,16,0.78));
#             padding: 16px;
#             border-radius: 12px;
#             color: #e6eef8;
#             margin-bottom: 18px;
#         }}
#         .mtg-small {{
#             color: #cbd7e6;
#             font-size: 14px;
#         }}
#         img.mtg-thumb {{
#             border-radius: 8px;
#             box-shadow: 0 6px 18px rgba(0,0,0,0.6);
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# # ----------------------------
# # 50+ gadgets dataset (hardcoded)
# # each entry: name, brand, category, price (USD string), image, specs, full_specs (optional)
# # Note: images are public-hosted product images
# # ----------------------------
# gadgets_data = [
#     # Phones (20)
#     {"name":"Samsung Galaxy S24 Ultra","brand":"Samsung","category":"Phone","price":"$1,199",
#      "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-1.jpg",
#      "specs":"6.8\" QHD+ AMOLED 120Hz • Snapdragon 8 Gen 3 • 12GB RAM • 5000mAh",
#      "full_specs": {"Display":"6.8\" QHD+ AMOLED 120Hz","SoC":"Snapdragon 8 Gen 3","RAM":"12GB","Battery":"5000 mAh","Camera":"200MP + 12MP + 10MP + 10MP"}},
#     {"name":"iPhone 15 Pro Max","brand":"Apple","category":"Phone","price":"$1,199",
#      "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg",
#      "specs":"6.7\" Super Retina XDR • A17 Pro • 8GB RAM • 4422mAh",
#      "full_specs": {"Display":"6.7\" Super Retina XDR","SoC":"Apple A17 Pro","RAM":"8GB","Battery":"4422 mAh","Camera":"48MP + 12MP + 12MP"}},
#     {"name":"Google Pixel 8 Pro","brand":"Google","category":"Phone","price":"$999",
#      "image":"https://fdn2.gsmarena.com/vv/pics/google/google-pixel-8-pro.jpg",
#      "specs":"6.7\" LTPO OLED 120Hz • Tensor G3 • 12GB RAM • 5050mAh",
#      "full_specs": {"Display":"6.7\" LTPO OLED","SoC":"Tensor G3","RAM":"12GB","Battery":"5050 mAh","Camera":"50MP + 48MP + 48MP"}},
#     {"name":"Xiaomi 14 Ultra","brand":"Xiaomi","category":"Phone","price":"$1,099",
#      "image":"https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-14-ultra.jpg",
#      "specs":"6.73\" AMOLED • Snapdragon 8 Gen 3 • 16GB RAM",
#      "full_specs": {"Display":"6.73\" AMOLED","SoC":"Snapdragon 8 Gen 3","RAM":"16GB","Battery":"5000 mAh","Camera":"Leica quad"}},
#     {"name":"OnePlus 12","brand":"OnePlus","category":"Phone","price":"$899",
#      "image":"https://fdn2.gsmarena.com/vv/pics/oneplus/oneplus-12.jpg",
#      "specs":"6.82\" AMOLED • Snapdragon 8 Gen 3 • 12GB RAM",
#      "full_specs": {"Display":"6.82\" AMOLED","SoC":"Snapdragon 8 Gen 3","RAM":"12GB","Battery":"5400 mAh","Camera":"50MP + 64MP + 48MP"}},
#     {"name":"Tecno Camon 30 Premier","brand":"Tecno","category":"Phone","price":"$499",
#      "image":"https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-premier.jpg",
#      "specs":"6.77\" AMOLED • Dimensity 8200 • 8/12GB RAM",
#      "full_specs": {"Display":"6.77\" AMOLED","SoC":"Dimensity 8200","RAM":"8/12GB","Battery":"5000 mAh","Camera":"50MP main"}},
#     {"name":"Infinix Zero Ultra 5G","brand":"Infinix","category":"Phone","price":"$499",
#      "image":"https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-ultra.jpg",
#      "specs":"6.8\" AMOLED • Dimensity 920 • 8/12GB RAM",
#      "full_specs": {"Display":"6.8\" AMOLED","SoC":"Dimensity 920","RAM":"8/12GB","Battery":"4500 mAh","Camera":"200MP main"}},
#     {"name":"Realme GT 7 Pro","brand":"Realme","category":"Phone","price":"$699",
#      "image":"https://fdn2.gsmarena.com/vv/pics/realme/realme-gt-7-pro.jpg",
#      "specs":"6.74\" AMOLED 144Hz • Snapdragon 8 Gen 3 • 12/16GB RAM",
#      "full_specs": {"Display":"6.74\" AMOLED 144Hz","SoC":"Snapdragon 8 Gen 3","RAM":"12/16GB","Battery":"4600 mAh","Camera":"50MP"}},
#     {"name":"Oppo Find X7 Pro","brand":"Oppo","category":"Phone","price":"$1,099",
#      "image":"https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-x7-pro.jpg",
#      "specs":"6.82\" QHD+ AMOLED • Snapdragon 8 Gen 3 • 12/16GB RAM",
#      "full_specs": {"Display":"6.82\" QHD+ AMOLED","SoC":"Snapdragon 8 Gen 3","RAM":"12/16GB","Battery":"5000 mAh","Camera":"Periscope zoom"}},
#     {"name":"Huawei Mate 70 Pro","brand":"Huawei","category":"Phone","price":"$1,099",
#      "image":"https://fdn2.gsmarena.com/vv/pics/huawei/huawei-mate-70-pro.jpg",
#      "specs":"6.82\" OLED • Kirin 9100 • 12GB RAM",
#      "full_specs": {"Display":"6.82\" OLED","SoC":"Kirin 9100","RAM":"12GB","Battery":"5100 mAh","Camera":"XMAGE"}},
#     {"name":"Vivo X100 Pro","brand":"Vivo","category":"Phone","price":"$999",
#      "image":"https://fdn2.gsmarena.com/vv/pics/vivo/vivo-x100-pro.jpg",
#      "specs":"6.78\" AMOLED • V2 chip • 12GB RAM",
#      "full_specs": {"Display":"6.78\" AMOLED","SoC":"V2","RAM":"12GB","Battery":"4900 mAh","Camera":"50MP"}},
#     {"name":"Sony Xperia 1 V","brand":"Sony","category":"Phone","price":"$1,199",
#      "image":"https://fdn2.gsmarena.com/vv/pics/sony/sony-xperia-1-v.jpg",
#      "specs":"6.5\" 4K HDR OLED • Snapdragon 8 Gen 2 • 12GB RAM",
#      "full_specs": {"Display":"6.5\" 4K HDR OLED","SoC":"Snapdragon 8 Gen 2","RAM":"12GB","Battery":"4500 mAh","Camera":"Multi-lens"}},
#     {"name":"Motorola Edge 50 Pro","brand":"Motorola","category":"Phone","price":"$599",
#      "image":"https://fdn2.gsmarena.com/vv/pics/motorola/motorola-edge-50-pro.jpg",
#      "specs":"6.67\" OLED • Snapdragon 7s Gen 2 • 12GB RAM",
#      "full_specs": {"Display":"6.67\" OLED","SoC":"Snapdragon 7s Gen 2","RAM":"12GB","Battery":"4600 mAh"}},
#     {"name":"Nokia X200","brand":"Nokia","category":"Phone","price":"$349",
#      "image":"https://fdn2.gsmarena.com/vv/pics/nokia/nokia-x200.jpg",
#      "specs":"6.6\" IPS • Helio G99 • 8GB RAM",
#      "full_specs": {"Display":"6.6\" IPS","SoC":"Helio G99","RAM":"8GB","Battery":"5000 mAh"}},
#     {"name":"Honor Magic6 Pro","brand":"Honor","category":"Phone","price":"$899",
#      "image":"https://fdn2.gsmarena.com/vv/pics/honor/honor-magic6-pro.jpg",
#      "specs":"6.8\" OLED • Snapdragon 8 Gen 3 • 12/16GB RAM",
#      "full_specs": {"Display":"6.8\" OLED","SoC":"Snapdragon 8 Gen 3","RAM":"12/16GB","Battery":"5000 mAh"}},
#     {"name":"Asus ROG Phone 8","brand":"Asus","category":"Phone","price":"$999",
#      "image":"https://fdn2.gsmarena.com/vv/pics/asus/asus-rog-phone-8.jpg",
#      "specs":"6.78\" AMOLED 144Hz • Snapdragon 8 Gen 3 • 16GB RAM",
#      "full_specs": {"Display":"6.78\" AMOLED 144Hz","SoC":"Snapdragon 8 Gen 3","RAM":"16GB","Battery":"6000 mAh"}},
#     {"name":"ZTE Axon 50","brand":"ZTE","category":"Phone","price":"$549",
#      "image":"https://fdn2.gsmarena.com/vv/pics/zte/zte-axon-50.jpg",
#      "specs":"6.67\" AMOLED • Snapdragon 7 Gen 3 • 12GB RAM",
#      "full_specs": {"Display":"6.67\" AMOLED","SoC":"Snapdragon 7 Gen 3","RAM":"12GB","Battery":"4800 mAh"}},
#     {"name":"Lenovo Legion Phone Duel","brand":"Lenovo","category":"Phone","price":"$799",
#      "image":"https://fdn2.gsmarena.com/vv/pics/lenovo/lenovo-legion-phone-duel.jpg",
#      "specs":"6.92\" AMOLED • Snapdragon 8 Gen • 12/16GB RAM",
#      "full_specs": {"Display":"6.92\" AMOLED","SoC":"Snapdragon 8 Gen","RAM":"12/16GB","Battery":"5500 mAh"}},
#     {"name":"Alcatel 1S (2024)","brand":"Alcatel","category":"Phone","price":"$119",
#      "image":"https://fdn2.gsmarena.com/vv/pics/alcatel/alcatel-1s.jpg",
#      "specs":"6.5\" IPS • Entry-level • 3/4GB RAM",
#      "full_specs": {"Display":"6.5\" IPS","SoC":"Entry SoC","RAM":"3/4GB","Battery":"4000 mAh"}},
#     {"name":"Poco F6","brand":"Poco","category":"Phone","price":"$399",
#      "image":"https://fdn2.gsmarena.com/vv/pics/poco/poco-f6.jpg",
#      "specs":"6.67\" AMOLED • Snapdragon 8s Gen 3 • 8/12GB RAM",
#      "full_specs": {"Display":"6.67\" AMOLED","SoC":"Snapdragon 8s Gen 3","RAM":"8/12GB","Battery":"5000 mAh"}},

#     # Laptops (10)
#     {"name":"MacBook Pro 16 (M3 Max)","brand":"Apple","category":"Laptop","price":"$3,499",
#      "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-macbook-pro-16.jpg",
#      "specs":"16\" Liquid Retina XDR • Apple M3 Max • 32GB RAM",
#      "full_specs": {"Display":"16\" Liquid Retina XDR","SoC":"M3 Max","RAM":"32GB","Storage":"1TB"}},
#     {"name":"MacBook Air 15 (M2)","brand":"Apple","category":"Laptop","price":"$1,299",
#      "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-macbook-air-15.jpg",
#      "specs":"15\" Retina • Apple M2 • 8/16GB RAM",
#      "full_specs": {"Display":"15\" Retina","SoC":"M2","RAM":"8/16GB","Storage":"512GB"}},
#     {"name":"Dell XPS 15","brand":"Dell","category":"Laptop","price":"$1,799",
#      "image":"https://fdn2.gsmarena.com/vv/pics/dell/dell-xps-15.jpg",
#      "specs":"15.6\" OLED • Intel i7 • 16GB RAM",
#      "full_specs": {"Display":"15.6\" OLED","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
#     {"name":"HP Spectre x360","brand":"HP","category":"Laptop","price":"$1,599",
#      "image":"https://fdn2.gsmarena.com/vv/pics/hp/hp-spectre-x360.jpg",
#      "specs":"13.5\" OLED • Intel i7 • 16GB RAM",
#      "full_specs": {"Display":"13.5\" OLED","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
#     {"name":"Lenovo ThinkPad X1 Carbon","brand":"Lenovo","category":"Laptop","price":"$1,499",
#      "image":"https://fdn2.gsmarena.com/vv/pics/lenovo/lenovo-thinkpad-x1.jpg",
#      "specs":"14\" IPS • Intel i7 • 16GB RAM",
#      "full_specs": {"Display":"14\" IPS","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
#     {"name":"Asus ROG Zephyrus G14","brand":"Asus","category":"Laptop","price":"$1,299",
#      "image":"https://fdn2.gsmarena.com/vv/pics/asus/asus-rog-zephyrus-g14.jpg",
#      "specs":"14\" 120Hz • Ryzen 9 • 16GB RAM",
#      "full_specs": {"Display":"14\" 120Hz","SoC":"Ryzen 9","RAM":"16GB","Storage":"1TB"}},
#     {"name":"Microsoft Surface Laptop 5","brand":"Microsoft","category":"Laptop","price":"$1,099",
#      "image":"https://fdn2.gsmarena.com/vv/pics/microsoft/surface-laptop-5.jpg",
#      "specs":"13.5\" PixelSense • Intel i7 • 16GB RAM",
#      "full_specs": {"Display":"13.5\" PixelSense","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
#     {"name":"Acer Swift 5","brand":"Acer","category":"Laptop","price":"$899",
#      "image":"https://fdn2.gsmarena.com/vv/pics/acer/acer-swift-5.jpg",
#      "specs":"14\" IPS • Intel i5 • 8/16GB RAM",
#      "full_specs": {"Display":"14\" IPS","SoC":"Intel i5","RAM":"8/16GB","Storage":"512GB"}},
#     {"name":"Razer Blade 14","brand":"Razer","category":"Laptop","price":"$1,799",
#      "image":"https://fdn2.gsmarena.com/vv/pics/razer/razer-blade-14.jpg",
#      "specs":"14\" 165Hz • Ryzen 9 • 16GB RAM",
#      "full_specs": {"Display":"14\" 165Hz","SoC":"Ryzen 9","RAM":"16GB","Storage":"1TB"}},
#     {"name":"LG Gram 17","brand":"LG","category":"Laptop","price":"$1,399",
#      "image":"https://fdn2.gsmarena.com/vv/pics/lg/lg-gram-17.jpg",
#      "specs":"17\" WQXGA • Intel i7 • 16GB RAM",
#      "full_specs": {"Display":"17\" WQXGA","SoC":"Intel i7","RAM":"16GB","Storage":"1TB"}},

#     # Tablets (8)
#     {"name":"iPad Pro 12.9 (M4)","brand":"Apple","category":"Tablet","price":"$1,099",
#      "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-12.9.jpg",
#      "specs":"12.9\" Liquid Retina XDR • Apple M4 • 8/16GB RAM",
#      "full_specs": {"Display":"12.9\" Liquid Retina XDR","SoC":"Apple M4","RAM":"8/16GB","Storage":"256/512GB"}},
#     {"name":"Samsung Galaxy Tab S9 Ultra","brand":"Samsung","category":"Tablet","price":"$1,099",
#      "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s9-ultra-1.jpg",
#      "specs":"14.6\" AMOLED • Snapdragon 8 Gen 2 • 12GB RAM",
#      "full_specs": {"Display":"14.6\" AMOLED","SoC":"Snapdragon 8 Gen 2","RAM":"12GB","Storage":"256/512GB"}},
#     {"name":"Xiaomi Pad 6 Pro","brand":"Xiaomi","category":"Tablet","price":"$499",
#      "image":"https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-pad-6-pro.jpg",
#      "specs":"11\" LCD • Snapdragon 8 Gen 1 • 8/12GB RAM",
#      "full_specs": {"Display":"11\" LCD","SoC":"Snapdragon 8 Gen 1","RAM":"8/12GB","Storage":"128/256GB"}},
#     {"name":"Lenovo Tab P12 Pro","brand":"Lenovo","category":"Tablet","price":"$599",
#      "image":"https://fdn2.gsmarena.com/vv/pics/lenovo/lenovo-tab-p12-pro.jpg",
#      "specs":"12.6\" AMOLED • Snapdragon 8 Gen 1 • 8GB RAM",
#      "full_specs": {"Display":"12.6\" AMOLED","SoC":"Snapdragon 8 Gen 1","RAM":"8GB","Storage":"128/256GB"}},
#     {"name":"Amazon Fire HD 10 (2023)","brand":"Amazon","category":"Tablet","price":"$149",
#      "image":"https://fdn2.gsmarena.com/vv/pics/amazon/amazon-fire-hd-10.jpg",
#      "specs":"10.1\" IPS • MediaTek • 3/4GB RAM",
#      "full_specs": {"Display":"10.1\" IPS","SoC":"MediaTek","RAM":"3/4GB","Storage":"32/64GB"}},
#     {"name":"Microsoft Surface Pro 9","brand":"Microsoft","category":"Tablet","price":"$999",
#      "image":"https://fdn2.gsmarena.com/vv/pics/microsoft/surface-pro-9.jpg",
#      "specs":"13\" PixelSense • Intel i7 • 16GB RAM",
#      "full_specs": {"Display":"13\" PixelSense","SoC":"Intel i7","RAM":"16GB","Storage":"256/512GB"}},
#     {"name":"Huawei MatePad Pro 13","brand":"Huawei","category":"Tablet","price":"$699",
#      "image":"https://fdn2.gsmarena.com/vv/pics/huawei/huawei-matepad-pro-13.jpg",
#      "specs":"13\" OLED • Kirin • 8GB RAM",
#      "full_specs": {"Display":"13\" OLED","SoC":"Kirin","RAM":"8GB","Storage":"128/256GB"}},
#     {"name":"Samsung Galaxy Tab A8","brand":"Samsung","category":"Tablet","price":"$229",
#      "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-a8.jpg",
#      "specs":"10.5\" TFT • Entry-level • 3/4GB RAM",
#      "full_specs": {"Display":"10.5\" TFT","SoC":"Entry SoC","RAM":"3/4GB","Storage":"32/64GB"}},

#     # Smartwatches (5)
#     {"name":"Apple Watch Ultra 2","brand":"Apple","category":"Smartwatch","price":"$799",
#      "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-watch-ultra-2.jpg",
#      "specs":"1.92\" OLED • S9 SiP • 36h battery",
#      "full_specs": {"Display":"1.92\" OLED","SoC":"S9 SiP","Battery":"36h"}},
#     {"name":"Samsung Galaxy Watch 6 Classic","brand":"Samsung","category":"Smartwatch","price":"$599",
#      "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-watch6-classic.jpg",
#      "specs":"1.5\" AMOLED • Exynos W930 • 40h battery",
#      "full_specs": {"Display":"1.5\" AMOLED","SoC":"Exynos W930","Battery":"40h"}},
#     {"name":"Fitbit Sense 2","brand":"Fitbit","category":"Smartwatch","price":"$299",
#      "image":"https://fdn2.gsmarena.com/vv/pics/fitbit/fitbit-sense-2.jpg",
#      "specs":"AMOLED • Health sensors • 6+ days battery",
#      "full_specs": {"Display":"AMOLED","Battery":"6+ days"}},
#     {"name":"Garmin Fenix 7","brand":"Garmin","category":"Smartwatch","price":"$699",
#      "image":"https://fdn2.gsmarena.com/vv/pics/garmin/garmin-fenix-7.jpg",
#      "specs":"Transflective • Outdoor GPS • 14+ days battery",
#      "full_specs": {"Display":"Transflective","Battery":"14+ days"}},
#     {"name":"Huawei Watch GT 4","brand":"Huawei","category":"Smartwatch","price":"$299",
#      "image":"https://fdn2.gsmarena.com/vv/pics/huawei/huawei-watch-gt-4.jpg",
#      "specs":"1.5\" AMOLED • HarmonyOS • 10+ days battery",
#      "full_specs": {"Display":"1.5\" AMOLED","Battery":"10+ days"}},

#     # Headphones / Earbuds (7)
#     {"name":"Sony WH-1000XM5","brand":"Sony","category":"Headphones","price":"$399",
#      "image":"https://fdn2.gsmarena.com/vv/pics/sony/sony-wh-1000xm5.jpg",
#      "specs":"Over-ear • ANC • 30h battery",
#      "full_specs": {"Type":"Over-ear","ANC":"Yes","Battery":"30h"}},
#     {"name":"Apple AirPods Pro (2nd Gen)","brand":"Apple","category":"Headphones","price":"$249",
#      "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-airpods-pro-2.jpg",
#      "specs":"In-ear • ANC • MagSafe charging case",
#      "full_specs": {"Type":"In-ear","ANC":"Yes","Battery":"6h + case"}},
#     {"name":"Bose QuietComfort Ultra","brand":"Bose","category":"Headphones","price":"$349",
#      "image":"https://fdn2.gsmarena.com/vv/pics/bose/bose-qc-ultra.jpg",
#      "specs":"Over-ear • ANC • 24h battery",
#      "full_specs": {"Type":"Over-ear","ANC":"Yes","Battery":"24h"}},
#     {"name":"Sennheiser Momentum 4","brand":"Sennheiser","category":"Headphones","price":"$349",
#      "image":"https://fdn2.gsmarena.com/vv/pics/sennheiser/sennheiser-momentum-4.jpg",
#      "specs":"Over-ear • Hi-Fi • 17h battery",
#      "full_specs": {"Type":"Over-ear","HiFi":"Yes","Battery":"17h"}},
#     {"name":"Jabra Elite 8 Active","brand":"Jabra","category":"Headphones","price":"$199",
#      "image":"https://fdn2.gsmarena.com/vv/pics/jabra/jabra-elite-8.jpg",
#      "specs":"In-ear • Sport • 24h battery",
#      "full_specs": {"Type":"In-ear","Sport":"Yes","Battery":"24h"}},
#     {"name":"Beats Studio Pro","brand":"Beats","category":"Headphones","price":"$349",
#      "image":"https://fdn2.gsmarena.com/vv/pics/beats/beats-studio-pro.jpg",
#      "specs":"Over-ear • Apple H2 chip • 22h battery",
#      "full_specs": {"Type":"Over-ear","Chip":"Apple H2","Battery":"22h"}},
#     {"name":"Anker Soundcore Liberty 4","brand":"Anker","category":"Headphones","price":"$129",
#      "image":"https://fdn2.gsmarena.com/vv/pics/anker/anker-soundcore-liberty-4.jpg",
#      "specs":"In-ear • ANC • 32h battery",
#      "full_specs": {"Type":"In-ear","ANC":"Yes","Battery":"32h"}},
# ]

# # ----------------------------
# # UI helpers
# # ----------------------------
# def show_gadget_card(g, usd_rate):
#     """Render single gadget card with thumbnail, short specs and a 'View Full Specs' expander"""
#     usd = price_usd_with_commas(g["price"])
#     ngn = convert_usd_to_ngn_str(g["price"], usd_rate)
#     st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
#     cols = st.columns([1, 2])
#     with cols[0]:
#         st.image(g["image"], width=180, use_column_width=False, output_format="auto")
#     with cols[1]:
#         st.markdown(f"### {g['name']}  •  {g['brand']}")
#         st.markdown(f"**Category:** {g['category']}")
#         st.markdown(f"**Specs (short):** {g['specs']}")
#         st.success(f"Price: {usd} | {ngn}")
#         # View full specs expander
#         with st.expander("View Full Specs"):
#             # if full_specs dict exists, show as a table-like list
#             fs = g.get("full_specs")
#             if isinstance(fs, dict):
#                 for k, v in fs.items():
#                     st.write(f"- **{k}:** {v}")
#             else:
#                 st.write(g.get("specs", "No further specs available."))
#     st.markdown('</div>', unsafe_allow_html=True)

# # ----------------------------
# # Sidebar / Navigation
# # ----------------------------
# st.sidebar.markdown("## 🔎 Controls")
# st.sidebar.write(f"1 USD ≈ ₦{usd_to_ngn_rate:,.0f}")
# st.sidebar.write(f"Rate last updated: {rate_last_updated}")
# st.sidebar.caption("Based on mid-market rates (cached hourly). Use Refresh to force an update.")

# menu = st.sidebar.radio("Navigate", ["Home", "Devices", "Compare", "About"])

# # apply background for current page
# apply_background(menu if menu in backgrounds else "Home")

# # ----------------------------
# # HOME PAGE
# # ----------------------------
# if menu == "Home":
#     st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
#     st.title("📱 Mobile Tech Gist")
#     st.write("Your GSMArena-style hub for gadgets — phones, laptops, tablets, watches & headphones.")
#     st.caption(f"💱 Live USD → NGN: 1 USD ≈ ₦{usd_to_ngn_rate:,.0f}  •  Last update: {rate_last_updated}")
#     st.markdown("</div>", unsafe_allow_html=True)

#     # Featured grid
#     st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
#     st.subheader("🔥 Featured Gadgets")
#     featured = gadgets_data[:6]
#     cols = st.columns(3)
#     for i, g in enumerate(featured):
#         with cols[i % 3]:
#             st.image(g["image"], width=220, caption=f"{g['name']} — {g['brand']}")
#             usd = price_usd_with_commas(g["price"])
#             ngn = convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate)
#             st.markdown(f"**{g['name']}**")
#             st.markdown(f"**Price:** {usd} | {ngn}")
#     st.markdown("</div>", unsafe_allow_html=True)

#     # Top picks (simple heuristic by price)
#     st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
#     st.subheader("⭐ Top Picks")
#     picks = sorted(gadgets_data, key=lambda x: float(x["price"].replace("$","").replace(",","")), reverse=True)[:4]
#     for g in picks:
#         usd = price_usd_with_commas(g["price"])
#         ngn = convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate)
#         st.markdown(f"**{g['name']}**  •  {g['brand']}  \nPrice: {usd} | {ngn}  \nSpecs: {g['specs']}")
#         st.write("---")
#     st.markdown("</div>", unsafe_allow_html=True)

# # ----------------------------
# # DEVICES PAGE
# # ----------------------------
# elif menu == "Devices":
#     st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
#     st.title("📚 Gadgets Catalog")
#     st.markdown("Search by name or brand, filter by category, and click 'View Full Specs' for deep details.")
#     st.markdown("</div>", unsafe_allow_html=True)

#     # Filters: search + category + brand (brand optional)
#     q_col, cat_col, brand_col = st.columns([3,1,1])
#     with q_col:
#         query = st.text_input("🔎 Search (name or brand)", "")
#     with cat_col:
#         category = st.selectbox("Category", ["All"] + sorted({g["category"] for g in gadgets_data}))
#     with brand_col:
#         brands = sorted({g["brand"] for g in gadgets_data})
#         brand = st.selectbox("Brand (optional)", ["All"] + brands)

#     # filtering
#     def match(g):
#         q = query.strip().lower()
#         if q:
#             if q not in g["name"].lower() and q not in g["brand"].lower():
#                 return False
#         if category != "All" and g["category"] != category:
#             return False
#         if brand != "All" and g["brand"] != brand:
#             return False
#         return True

#     results = [g for g in gadgets_data if match(g)]
#     st.write(f"Found **{len(results)}** gadgets.")

#     # pagination-like chunk display to keep UI responsive
#     for g in results:
#         show_gadget_card(g, usd_to_ngn_rate)

# # ----------------------------
# # COMPARE PAGE (up to 3 gadgets)
# # ----------------------------
# elif menu == "Compare":
#     st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
#     st.title("⚖️ Compare Gadgets (choose up to 3)")
#     st.write("Pick up to 3 gadgets to compare side-by-side. Use search below to quickly find items.")
#     st.markdown("</div>", unsafe_allow_html=True)

#     # multi-select with search-friendly list
#     all_names = [g["name"] for g in gadgets_data]
#     selected = st.multiselect("Select gadgets to compare (2 or 3 recommended)", all_names, default=all_names[:2], max_selections=3)

#     if selected:
#         picked = [g for g in gadgets_data if g["name"] in selected]
#         # thumbnails row
#         cols = st.columns(len(picked))
#         for i, g in enumerate(picked):
#             with cols[i]:
#                 st.image(g["image"], width=160)
#                 st.markdown(f"**{g['name']}**")
#                 st.caption(f"{g['brand']}")
#                 usd = price_usd_with_commas(g["price"])
#                 ngn = convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate)
#                 st.write(f"**Price:** {usd} | {ngn}")

#         # Build comparison DataFrame-like table (rows = key fields)
#         comp_rows = {}
#         for g in picked:
#             comp_rows[g["name"]] = {
#                 "Brand": g["brand"],
#                 "Category": g["category"],
#                 "Price (USD)": price_usd_with_commas(g["price"]),
#                 "Price (NGN)": convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate),
#                 "Short Specs": g["specs"]
#             }
#         df = pd.DataFrame(comp_rows).T
#         st.markdown("### 📑 Quick Comparison Table")
#         st.table(df)

#         # Full specs expanders for each
#         st.markdown("### 🔎 Full Specs")
#         for g in picked:
#             with st.expander(f"{g['name']} — Full Specs"):
#                 fs = g.get("full_specs")
#                 if isinstance(fs, dict):
#                     for k, v in fs.items():
#                         st.write(f"- **{k}:** {v}")
#                 else:
#                     st.write(g.get("specs", "No further specs available."))

# # ----------------------------
# # ABOUT
# # ----------------------------
# elif menu == "About":
#     st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
#     st.title("About Mobile Tech Gist")
#     st.write(
#         "Mobile Tech Gist is a compact GSMArena-style demo built with Streamlit. "
#         "It showcases 50+ gadgets (phones, laptops, tablets, smartwatches and headphones) "
#         "with live USD→NGN pricing, images, search & compare features."
#     )
#     st.markdown("</div>", unsafe_allow_html=True)

# # Footer note
# st.markdown("<br>", unsafe_allow_html=True)
# st.markdown('<div class="mtg-small">Built with ❤️ — prices are mid-market conversions and update hourly. Images load from public image hosts.</div>', unsafe_allow_html=True)


import streamlit as st
import requests
import datetime
import pandas as pd

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(page_title="Mobile Tech Gist", layout="wide", page_icon="📱")

# ----------------------------
# Exchange rate (cached)
# ----------------------------
@st.cache_data(ttl=3600)
def fetch_usd_to_ngn():
    """Fetch USD -> NGN (no API key). Returns (rate, last_update_str)."""
    try:
        # exchangerate.host is free and requires no API key
        r = requests.get("https://api.exchangerate.host/latest?base=USD&symbols=NGN", timeout=8)
        data = r.json()
        rate = data.get("rates", {}).get("NGN")
        ts = data.get("timestamp") or data.get("date")
        if rate is None:
            raise ValueError("No rate")
        if isinstance(ts, int):
            last = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
        else:
            last = str(ts)
        return float(rate), last
    except Exception:
        # fallback conservative default
        return 1600.0, "Unavailable (fallback)"

def convert_usd_to_ngn_str(price_usd_str, rate):
    try:
        val = float(price_usd_str.replace("$", "").replace(",", "").strip())
        ngn = val * rate
        return f"₦{ngn:,.0f}"
    except Exception:
        return "₦---"

def price_usd_with_commas(price_str):
    try:
        v = float(price_str.replace("$","").replace(",",""))
        return f"${v:,.0f}"
    except:
        return price_str

# manual refresh button in sidebar
if st.sidebar.button("🔄 Refresh exchange rate"):
    st.cache_data.clear()

usd_to_ngn_rate, rate_last_updated = fetch_usd_to_ngn()

# ----------------------------
# Backgrounds (real gadget showcase; less dimmed)
# hosted online
# ----------------------------
backgrounds = {
    "Home": "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1600&auto=format&fit=crop&sat=-30",
    "Devices": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?q=80&w=1600&auto=format&fit=crop&sat=-30",
    "Compare": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?q=80&w=1600&auto=format&fit=crop&sat=-30",
    "About": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?q=80&w=1600&auto=format&fit=crop&sat=-30",
}

def apply_background(page_key):
    """Apply background image with a less dimming overlay."""
    url = backgrounds.get(page_key)
    if not url:
        return
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(4,8,16,0.6), rgba(4,8,16,0.6)), url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #e6eef8;
        }}
        /* translucent card for readable content */
        .mtg-card {{
            background: linear-gradient(rgba(4,8,16,0.65), rgba(4,8,16,0.65));
            padding: 16px;
            border-radius: 12px;
            color: #e6eef8;
            margin-bottom: 18px;
        }}
        .mtg-small {{
            color: #cbd7e6;
            font-size: 14px;
        }}
        img.mtg-thumb {{
            border-radius: 8px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.6);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# 50+ gadgets dataset (hardcoded)
# each entry: name, brand, category, price (USD string), image, specs, full_specs (optional)
# Note: images are public-hosted product images
# ----------------------------
gadgets_data = [
    # Phones (20)
    {"name":"Samsung Galaxy S24 Ultra","brand":"Samsung","category":"Phone","price":"$1,199",
    "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s24-ultra-1.jpg",
    "specs":"6.8\" QHD+ AMOLED 120Hz • Snapdragon 8 Gen 3 • 12GB RAM • 5000mAh",
    "full_specs": {"Display":"6.8\" QHD+ AMOLED 120Hz","SoC":"Snapdragon 8 Gen 3","RAM":"12GB","Battery":"5000 mAh","Camera":"200MP + 12MP + 10MP + 10MP"}},
    {"name":"iPhone 15 Pro Max","brand":"Apple","category":"Phone","price":"$1,199",
    "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-15-pro-max-1.jpg",
    "specs":"6.7\" Super Retina XDR • A17 Pro • 8GB RAM • 4422mAh",
    "full_specs": {"Display":"6.7\" Super Retina XDR","SoC":"Apple A17 Pro","RAM":"8GB","Battery":"4422 mAh","Camera":"48MP + 12MP + 12MP"}},
    {"name":"Google Pixel 8 Pro","brand":"Google","category":"Phone","price":"$999",
    "image":"https://fdn2.gsmarena.com/vv/pics/google/google-pixel-8-pro.jpg",
    "specs":"6.7\" LTPO OLED 120Hz • Tensor G3 • 12GB RAM • 5050mAh",
    "full_specs": {"Display":"6.7\" LTPO OLED","SoC":"Tensor G3","RAM":"12GB","Battery":"5050 mAh","Camera":"50MP + 48MP + 48MP"}},
    {"name":"Xiaomi 14 Ultra","brand":"Xiaomi","category":"Phone","price":"$1,099",
    "image":"https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-14-ultra.jpg",
    "specs":"6.73\" AMOLED • Snapdragon 8 Gen 3 • 16GB RAM",
    "full_specs": {"Display":"6.73\" AMOLED","SoC":"Snapdragon 8 Gen 3","RAM":"16GB","Battery":"5000 mAh","Camera":"Leica quad"}},
    {"name":"OnePlus 12","brand":"OnePlus","category":"Phone","price":"$899",
    "image":"https://fdn2.gsmarena.com/vv/pics/oneplus/oneplus-12.jpg",
    "specs":"6.82\" AMOLED • Snapdragon 8 Gen 3 • 12GB RAM",
    "full_specs": {"Display":"6.82\" AMOLED","SoC":"Snapdragon 8 Gen 3","RAM":"12GB","Battery":"5400 mAh","Camera":"50MP + 64MP + 48MP"}},
    {"name":"Tecno Camon 30 Premier","brand":"Tecno","category":"Phone","price":"$499",
    "image":"https://fdn2.gsmarena.com/vv/pics/tecno/tecno-camon-30-premier.jpg",
    "specs":"6.77\" AMOLED • Dimensity 8200 • 8/12GB RAM",
    "full_specs": {"Display":"6.77\" AMOLED","SoC":"Dimensity 8200","RAM":"8/12GB","Battery":"5000 mAh","Camera":"50MP main"}},
    {"name":"Infinix Zero Ultra 5G","brand":"Infinix","category":"Phone","price":"$499",
    "image":"https://fdn2.gsmarena.com/vv/pics/infinix/infinix-zero-ultra.jpg",
    "specs":"6.8\" AMOLED • Dimensity 920 • 8/12GB RAM",
    "full_specs": {"Display":"6.8\" AMOLED","SoC":"Dimensity 920","RAM":"8/12GB","Battery":"4500 mAh","Camera":"200MP main"}},
    {"name":"Realme GT 7 Pro","brand":"Realme","category":"Phone","price":"$699",
    "image":"https://fdn2.gsmarena.com/vv/pics/realme/realme-gt-7-pro.jpg",
    "specs":"6.74\" AMOLED 144Hz • Snapdragon 8 Gen 3 • 12/16GB RAM",
    "full_specs": {"Display":"6.74\" AMOLED 144Hz","SoC":"Snapdragon 8 Gen 3","RAM":"12/16GB","Battery":"4600 mAh","Camera":"50MP"}},
    {"name":"Oppo Find X7 Pro","brand":"Oppo","category":"Phone","price":"$1,099",
    "image":"https://fdn2.gsmarena.com/vv/pics/oppo/oppo-find-x7-pro.jpg",
    "specs":"6.82\" QHD+ AMOLED • Snapdragon 8 Gen 3 • 12/16GB RAM",
    "full_specs": {"Display":"6.82\" QHD+ AMOLED","SoC":"Snapdragon 8 Gen 3","RAM":"12/16GB","Battery":"5000 mAh","Camera":"Periscope zoom"}},
    {"name":"Huawei Mate 70 Pro","brand":"Huawei","category":"Phone","price":"$1,099",
    "image":"https://fdn2.gsmarena.com/vv/pics/huawei/huawei-mate-70-pro.jpg",
    "specs":"6.82\" OLED • Kirin 9100 • 12GB RAM",
    "full_specs": {"Display":"6.82\" OLED","SoC":"Kirin 9100","RAM":"12GB","Battery":"5100 mAh","Camera":"XMAGE"}},
    {"name":"Vivo X100 Pro","brand":"Vivo","category":"Phone","price":"$999",
    "image":"https://fdn2.gsmarena.com/vv/pics/vivo/vivo-x100-pro.jpg",
    "specs":"6.78\" AMOLED • V2 chip • 12GB RAM",
    "full_specs": {"Display":"6.78\" AMOLED","SoC":"V2","RAM":"12GB","Battery":"4900 mAh","Camera":"50MP"}},
    {"name":"Sony Xperia 1 V","brand":"Sony","category":"Phone","price":"$1,199",
    "image":"https://fdn2.gsmarena.com/vv/pics/sony/sony-xperia-1-v.jpg",
    "specs":"6.5\" 4K HDR OLED • Snapdragon 8 Gen 2 • 12GB RAM",
    "full_specs": {"Display":"6.5\" 4K HDR OLED","SoC":"Snapdragon 8 Gen 2","RAM":"12GB","Battery":"4500 mAh","Camera":"Multi-lens"}},
    {"name":"Motorola Edge 50 Pro","brand":"Motorola","category":"Phone","price":"$599",
    "image":"https://fdn2.gsmarena.com/vv/pics/motorola/motorola-edge-50-pro.jpg",
    "specs":"6.67\" OLED • Snapdragon 7s Gen 2 • 12GB RAM",
    "full_specs": {"Display":"6.67\" OLED","SoC":"Snapdragon 7s Gen 2","RAM":"12GB","Battery":"4600 mAh"}},
    {"name":"Nokia X200","brand":"Nokia","category":"Phone","price":"$349",
    "image":"https://fdn2.gsmarena.com/vv/pics/nokia/nokia-x200.jpg",
    "specs":"6.6\" IPS • Helio G99 • 8GB RAM",
    "full_specs": {"Display":"6.6\" IPS","SoC":"Helio G99","RAM":"8GB","Battery":"5000 mAh"}},
    {"name":"Honor Magic6 Pro","brand":"Honor","category":"Phone","price":"$899",
    "image":"https://fdn2.gsmarena.com/vv/pics/honor/honor-magic6-pro.jpg",
    "specs":"6.8\" OLED • Snapdragon 8 Gen 3 • 12/16GB RAM",
    "full_specs": {"Display":"6.8\" OLED","SoC":"Snapdragon 8 Gen 3","RAM":"12/16GB","Battery":"5000 mAh"}},
    {"name":"Asus ROG Phone 8","brand":"Asus","category":"Phone","price":"$999",
    "image":"https://fdn2.gsmarena.com/vv/pics/asus/asus-rog-phone-8.jpg",
    "specs":"6.78\" AMOLED 144Hz • Snapdragon 8 Gen 3 • 16GB RAM",
    "full_specs": {"Display":"6.78\" AMOLED 144Hz","SoC":"Snapdragon 8 Gen 3","RAM":"16GB","Battery":"6000 mAh"}},
    {"name":"ZTE Axon 50","brand":"ZTE","category":"Phone","price":"$549",
    "image":"https://fdn2.gsmarena.com/vv/pics/zte/zte-axon-50.jpg",
    "specs":"6.67\" AMOLED • Snapdragon 7 Gen 3 • 12GB RAM",
    "full_specs": {"Display":"6.67\" AMOLED","SoC":"Snapdragon 7 Gen 3","RAM":"12GB","Battery":"4800 mAh"}},
    {"name":"Lenovo Legion Phone Duel","brand":"Lenovo","category":"Phone","price":"$799",
    "image":"https://fdn2.gsmarena.com/vv/pics/lenovo/lenovo-legion-phone-duel.jpg",
    "specs":"6.92\" AMOLED • Snapdragon 8 Gen • 12/16GB RAM",
    "full_specs": {"Display":"6.92\" AMOLED","SoC":"Snapdragon 8 Gen","RAM":"12/16GB","Battery":"5500 mAh"}},
    {"name":"Alcatel 1S (2024)","brand":"Alcatel","category":"Phone","price":"$119",
    "image":"https://fdn2.gsmarena.com/vv/pics/alcatel/alcatel-1s.jpg",
    "specs":"6.5\" IPS • Entry-level • 3/4GB RAM",
    "full_specs": {"Display":"6.5\" IPS","SoC":"Entry SoC","RAM":"3/4GB","Battery":"4000 mAh"}},
    {"name":"Poco F6","brand":"Poco","category":"Phone","price":"$399",
    "image":"https://fdn2.gsmarena.com/vv/pics/poco/poco-f6.jpg",
    "specs":"6.67\" AMOLED • Snapdragon 8s Gen 3 • 8/12GB RAM",
    "full_specs": {"Display":"6.67\" AMOLED","SoC":"Snapdragon 8s Gen 3","RAM":"8/12GB","Battery":"5000 mAh"}},

    # Laptops (10)
    {"name":"MacBook Pro 16 (M3 Max)","brand":"Apple","category":"Laptop","price":"$3,499",
    "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-macbook-pro-16.jpg",
    "specs":"16\" Liquid Retina XDR • Apple M3 Max • 32GB RAM",
    "full_specs": {"Display":"16\" Liquid Retina XDR","SoC":"M3 Max","RAM":"32GB","Storage":"1TB"}},
    {"name":"MacBook Air 15 (M2)","brand":"Apple","category":"Laptop","price":"$1,299",
    "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-macbook-air-15.jpg",
    "specs":"15\" Retina • Apple M2 • 8/16GB RAM",
    "full_specs": {"Display":"15\" Retina","SoC":"M2","RAM":"8/16GB","Storage":"512GB"}},
    {"name":"Dell XPS 15","brand":"Dell","category":"Laptop","price":"$1,799",
    "image":"https://fdn2.gsmarena.com/vv/pics/dell/dell-xps-15.jpg",
    "specs":"15.6\" OLED • Intel i7 • 16GB RAM",
    "full_specs": {"Display":"15.6\" OLED","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
    {"name":"HP Spectre x360","brand":"HP","category":"Laptop","price":"$1,599",
    "image":"https://fdn2.gsmarena.com/vv/pics/hp/hp-spectre-x360.jpg",
    "specs":"13.5\" OLED • Intel i7 • 16GB RAM",
    "full_specs": {"Display":"13.5\" OLED","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
    {"name":"Lenovo ThinkPad X1 Carbon","brand":"Lenovo","category":"Laptop","price":"$1,499",
    "image":"https://fdn2.gsmarena.com/vv/pics/lenovo/lenovo-thinkpad-x1.jpg",
    "specs":"14\" IPS • Intel i7 • 16GB RAM",
    "full_specs": {"Display":"14\" IPS","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
    {"name":"Asus ROG Zephyrus G14","brand":"Asus","category":"Laptop","price":"$1,299",
    "image":"https://fdn2.gsmarena.com/vv/pics/asus/asus-rog-zephyrus-g14.jpg",
    "specs":"14\" 120Hz • Ryzen 9 • 16GB RAM",
    "full_specs": {"Display":"14\" 120Hz","SoC":"Ryzen 9","RAM":"16GB","Storage":"1TB"}},
    {"name":"Microsoft Surface Laptop 5","brand":"Microsoft","category":"Laptop","price":"$1,099",
    "image":"https://fdn2.gsmarena.com/vv/pics/microsoft/surface-laptop-5.jpg",
    "specs":"13.5\" PixelSense • Intel i7 • 16GB RAM",
    "full_specs": {"Display":"13.5\" PixelSense","SoC":"Intel i7","RAM":"16GB","Storage":"512GB"}},
    {"name":"Acer Swift 5","brand":"Acer","category":"Laptop","price":"$899",
    "image":"https://fdn2.gsmarena.com/vv/pics/acer/acer-swift-5.jpg",
    "specs":"14\" IPS • Intel i5 • 8/16GB RAM",
    "full_specs": {"Display":"14\" IPS","SoC":"Intel i5","RAM":"8/16GB","Storage":"512GB"}},
    {"name":"Razer Blade 14","brand":"Razer","category":"Laptop","price":"$1,799",
    "image":"https://fdn2.gsmarena.com/vv/pics/razer/razer-blade-14.jpg",
    "specs":"14\" 165Hz • Ryzen 9 • 16GB RAM",
    "full_specs": {"Display":"14\" 165Hz","SoC":"Ryzen 9","RAM":"16GB","Storage":"1TB"}},
    {"name":"LG Gram 17","brand":"LG","category":"Laptop","price":"$1,399",
    "image":"https://fdn2.gsmarena.com/vv/pics/lg/lg-gram-17.jpg",
    "specs":"17\" WQXGA • Intel i7 • 16GB RAM",
    "full_specs": {"Display":"17\" WQXGA","SoC":"Intel i7","RAM":"16GB","Storage":"1TB"}},

    # Tablets (8)
    {"name":"iPad Pro 12.9 (M4)","brand":"Apple","category":"Tablet","price":"$1,099",
    "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-ipad-pro-12.9.jpg",
    "specs":"12.9\" Liquid Retina XDR • Apple M4 • 8/16GB RAM",
    "full_specs": {"Display":"12.9\" Liquid Retina XDR","SoC":"Apple M4","RAM":"8/16GB","Storage":"256/512GB"}},
    {"name":"Samsung Galaxy Tab S9 Ultra","brand":"Samsung","category":"Tablet","price":"$1,099",
    "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-s9-ultra-1.jpg",
    "specs":"14.6\" AMOLED • Snapdragon 8 Gen 2 • 12GB RAM",
    "full_specs": {"Display":"14.6\" AMOLED","SoC":"Snapdragon 8 Gen 2","RAM":"12GB","Storage":"256/512GB"}},
    {"name":"Xiaomi Pad 6 Pro","brand":"Xiaomi","category":"Tablet","price":"$499",
    "image":"https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-pad-6-pro.jpg",
    "specs":"11\" LCD • Snapdragon 8 Gen 1 • 8/12GB RAM",
    "full_specs": {"Display":"11\" LCD","SoC":"Snapdragon 8 Gen 1","RAM":"8/12GB","Storage":"128/256GB"}},
    {"name":"Lenovo Tab P12 Pro","brand":"Lenovo","category":"Tablet","price":"$599",
    "image":"https://fdn2.gsmarena.com/vv/pics/lenovo/lenovo-tab-p12-pro.jpg",
    "specs":"12.6\" AMOLED • Snapdragon 8 Gen 1 • 8GB RAM",
    "full_specs": {"Display":"12.6\" AMOLED","SoC":"Snapdragon 8 Gen 1","RAM":"8GB","Storage":"128/256GB"}},
    {"name":"Amazon Fire HD 10 (2023)","brand":"Amazon","category":"Tablet","price":"$149",
    "image":"https://fdn2.gsmarena.com/vv/pics/amazon/amazon-fire-hd-10.jpg",
    "specs":"10.1\" IPS • MediaTek • 3/4GB RAM",
    "full_specs": {"Display":"10.1\" IPS","SoC":"MediaTek","RAM":"3/4GB","Storage":"32/64GB"}},
    {"name":"Microsoft Surface Pro 9","brand":"Microsoft","category":"Tablet","price":"$999",
    "image":"https://fdn2.gsmarena.com/vv/pics/microsoft/surface-pro-9.jpg",
    "specs":"13\" PixelSense • Intel i7 • 16GB RAM",
    "full_specs": {"Display":"13\" PixelSense","SoC":"Intel i7","RAM":"16GB","Storage":"256/512GB"}},
    {"name":"Huawei MatePad Pro 13","brand":"Huawei","category":"Tablet","price":"$699",
    "image":"https://fdn2.gsmarena.com/vv/pics/huawei/huawei-matepad-pro-13.jpg",
    "specs":"13\" OLED • Kirin • 8GB RAM",
    "full_specs": {"Display":"13\" OLED","SoC":"Kirin","RAM":"8GB","Storage":"128/256GB"}},
    {"name":"Samsung Galaxy Tab A8","brand":"Samsung","category":"Tablet","price":"$229",
    "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-tab-a8.jpg",
    "specs":"10.5\" TFT • Entry-level • 3/4GB RAM",
    "full_specs": {"Display":"10.5\" TFT","SoC":"Entry SoC","RAM":"3/4GB","Storage":"32/64GB"}},

    # Smartwatches (5)
    {"name":"Apple Watch Ultra 2","brand":"Apple","category":"Smartwatch","price":"$799",
    "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-watch-ultra-2.jpg",
    "specs":"1.92\" OLED • S9 SiP • 36h battery",
    "full_specs": {"Display":"1.92\" OLED","SoC":"S9 SiP","Battery":"36h"}},
    {"name":"Samsung Galaxy Watch 6 Classic","brand":"Samsung","category":"Smartwatch","price":"$599",
    "image":"https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-watch6-classic.jpg",
    "specs":"1.5\" AMOLED • Exynos W930 • 40h battery",
    "full_specs": {"Display":"1.5\" AMOLED","SoC":"Exynos W930","Battery":"40h"}},
    {"name":"Fitbit Sense 2","brand":"Fitbit","category":"Smartwatch","price":"$299",
    "image":"https://fdn2.gsmarena.com/vv/pics/fitbit/fitbit-sense-2.jpg",
    "specs":"AMOLED • Health sensors • 6+ days battery",
    "full_specs": {"Display":"AMOLED","Battery":"6+ days"}},
    {"name":"Garmin Fenix 7","brand":"Garmin","category":"Smartwatch","price":"$699",
    "image":"https://fdn2.gsmarena.com/vv/pics/garmin/garmin-fenix-7.jpg",
    "specs":"Transflective • Outdoor GPS • 14+ days battery",
    "full_specs": {"Display":"Transflective","Battery":"14+ days"}},
    {"name":"Huawei Watch GT 4","brand":"Huawei","category":"Smartwatch","price":"$299",
    "image":"https://fdn2.gsmarena.com/vv/pics/huawei/huawei-watch-gt-4.jpg",
    "specs":"1.5\" AMOLED • HarmonyOS • 10+ days battery",
    "full_specs": {"Display":"1.5\" AMOLED","Battery":"10+ days"}},

    # Headphones / Earbuds (7)
    {"name":"Sony WH-1000XM5","brand":"Sony","category":"Headphones","price":"$399",
    "image":"https://fdn2.gsmarena.com/vv/pics/sony/sony-wh-1000xm5.jpg",
    "specs":"Over-ear • ANC • 30h battery",
    "full_specs": {"Type":"Over-ear","ANC":"Yes","Battery":"30h"}},
    {"name":"Apple AirPods Pro (2nd Gen)","brand":"Apple","category":"Headphones","price":"$249",
    "image":"https://fdn2.gsmarena.com/vv/pics/apple/apple-airpods-pro-2.jpg",
    "specs":"In-ear • ANC • MagSafe charging case",
    "full_specs": {"Type":"In-ear","ANC":"Yes","Battery":"6h + case"}},
    {"name":"Bose QuietComfort Ultra","brand":"Bose","category":"Headphones","price":"$349",
    "image":"https://fdn2.gsmarena.com/vv/pics/bose/bose-qc-ultra.jpg",
    "specs":"Over-ear • ANC • 24h battery",
    "full_specs": {"Type":"Over-ear","ANC":"Yes","Battery":"24h"}},
    {"name":"Sennheiser Momentum 4","brand":"Sennheiser","category":"Headphones","price":"$349",
    "image":"https://fdn2.gsmarena.com/vv/pics/sennheiser/sennheiser-momentum-4.jpg",
    "specs":"Over-ear • Hi-Fi • 17h battery",
    "full_specs": {"Type":"Over-ear","HiFi":"Yes","Battery":"17h"}},
    {"name":"Jabra Elite 8 Active","brand":"Jabra","category":"Headphones","price":"$199",
    "image":"https://fdn2.gsmarena.com/vv/pics/jabra/jabra-elite-8.jpg",
    "specs":"In-ear • Sport • 24h battery",
    "full_specs": {"Type":"In-ear","Sport":"Yes","Battery":"24h"}},
    {"name":"Beats Studio Pro","brand":"Beats","category":"Headphones","price":"$349",
    "image":"https://fdn2.gsmarena.com/vv/pics/beats/beats-studio-pro.jpg",
    "specs":"Over-ear • Apple H2 chip • 22h battery",
    "full_specs": {"Type":"Over-ear","Chip":"Apple H2","Battery":"22h"}},
    {"name":"Anker Soundcore Liberty 4","brand":"Anker","category":"Headphones","price":"$129",
    "image":"https://fdn2.gsmarena.com/vv/pics/anker/anker-soundcore-liberty-4.jpg",
    "specs":"In-ear • ANC • 32h battery",
    "full_specs": {"Type":"In-ear","ANC":"Yes","Battery":"32h"}},
]

# ----------------------------
# UI helpers
# ----------------------------
def show_gadget_card(g, usd_rate):
    """Render single gadget card with thumbnail, short specs and a 'View Full Specs' expander"""
    usd = price_usd_with_commas(g["price"])
    ngn = convert_usd_to_ngn_str(g["price"], usd_rate)
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    
    # Display image first, without columns, so it always shows
    st.image(g["image"], use_container_width=False, output_format="auto")
    st.markdown(f"### {g['name']}  •  {g['brand']}")
    st.markdown(f"**Category:** {g['category']}")
    st.markdown(f"**Specs (short):** {g['specs']}")
    st.success(f"Price: {usd} | {ngn}")
    
    # View full specs expander
    with st.expander("View Full Specs"):
        fs = g.get("full_specs")
        if isinstance(fs, dict):
            for k, v in fs.items():
                st.write(f"- **{k}:** {v}")
        else:
            st.write(g.get("specs", "No further specs available."))
    st.markdown('</div>', unsafe_allow_html=True)

# ----------------------------
# Sidebar / Navigation
# ----------------------------
st.sidebar.markdown("## 🔎 Controls")
st.sidebar.write(f"1 USD ≈ ₦{usd_to_ngn_rate:,.0f}")
st.sidebar.write(f"Rate last updated: {rate_last_updated}")
st.sidebar.caption("Based on mid-market rates (cached hourly). Use Refresh to force an update.")

menu = st.sidebar.radio("Navigate", ["Home", "Devices", "Compare", "About"])

# apply background for current page
apply_background(menu if menu in backgrounds else "Home")

# ----------------------------
# HOME PAGE
# ----------------------------
if menu == "Home":
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.title("📱 Mobile Tech Gist")
    st.write("Your GSMArena-style hub for gadgets — phones, laptops, tablets, watches & headphones.")
    st.caption(f"💱 Live USD → NGN: 1 USD ≈ ₦{usd_to_ngn_rate:,.0f}  •  Last update: {rate_last_updated}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Summary Stats Section
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.subheader("📊 At a Glance")
    total_gadgets = len(gadgets_data)
    category_counts = pd.DataFrame(gadgets_data)['category'].value_counts()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Gadgets", value=total_gadgets)
    with col2:
        st.write("#### By Category")
        st.dataframe(category_counts.rename("Count"), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Featured grid
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.subheader("🔥 Featured Gadgets")
    featured = gadgets_data[:6]
    cols = st.columns(3)
    for i, g in enumerate(featured):
        with cols[i % 3]:
            st.image(g["image"], use_container_width=True, caption=f"{g['name']} — {g['brand']}")
            usd = price_usd_with_commas(g["price"])
            ngn = convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate)
            st.markdown(f"**{g['name']}**")
            st.markdown(f"**Price:** {usd} | {ngn}")
    st.markdown("</div>", unsafe_allow_html=True)

    # Top picks (simple heuristic by price)
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.subheader("⭐ Top Picks")
    picks = sorted(gadgets_data, key=lambda x: float(x["price"].replace("$","").replace(",","")), reverse=True)[:4]
    for g in picks:
        usd = price_usd_with_commas(g["price"])
        ngn = convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate)
        st.markdown(f"**{g['name']}** •  {g['brand']}  \nPrice: {usd} | {ngn}  \nSpecs: {g['specs']}")
        st.write("---")
    st.markdown("</div>", unsafe_allow_html=True)

    # New Arrivals Section
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.subheader("✨ New Arrivals")
    new_arrivals = gadgets_data[-3:]  # Get the last 3 items
    cols = st.columns(3)
    for i, g in enumerate(new_arrivals):
        with cols[i]:
            st.image(g["image"], use_container_width=True, caption=g['name'])
            usd = price_usd_with_commas(g["price"])
            ngn = convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate)
            st.markdown(f"**{g['name']}**")
            st.markdown(f"Price: {usd} | {ngn}")
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# DEVICES PAGE
# ----------------------------
elif menu == "Devices":
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.title("📚 Gadgets Catalog")
    st.markdown("Search by name or brand, filter by category, and click 'View Full Specs' for deep details.")
    st.markdown("</div>", unsafe_allow_html=True)

    # Filters: search + category + brand (brand optional)
    q_col, cat_col, brand_col = st.columns([3,1,1])
    with q_col:
        query = st.text_input("🔎 Search (name or brand)", "")
    with cat_col:
        category = st.selectbox("Category", ["All"] + sorted({g["category"] for g in gadgets_data}))
    with brand_col:
        brands = sorted({g["brand"] for g in gadgets_data})
        brand = st.selectbox("Brand (optional)", ["All"] + brands)

    # filtering
    def match(g):
        q = query.strip().lower()
        if q:
            if q not in g["name"].lower() and q not in g["brand"].lower():
                return False
        if category != "All" and g["category"] != category:
            return False
        if brand != "All" and g["brand"] != brand:
            return False
        return True

    results = [g for g in gadgets_data if match(g)]
    st.write(f"Found **{len(results)}** gadgets.")

    # pagination-like chunk display to keep UI responsive
    for g in results:
        show_gadget_card(g, usd_to_ngn_rate)

# ----------------------------
# COMPARE PAGE (up to 3 gadgets)
# ----------------------------
elif menu == "Compare":
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.title("⚖️ Compare Gadgets (choose up to 3)")
    st.write("Pick up to 3 gadgets to compare side-by-side. Use search below to quickly find items.")
    st.markdown("</div>", unsafe_allow_html=True)

    # multi-select with search-friendly list
    all_names = [g["name"] for g in gadgets_data]
    selected = st.multiselect("Select gadgets to compare (2 or 3 recommended)", all_names, default=all_names[:2], max_selections=3)

    if selected:
        picked = [g for g in gadgets_data if g["name"] in selected]
        # thumbnails row
        cols = st.columns(len(picked))
        for i, g in enumerate(picked):
            with cols[i]:
                st.image(g["image"], use_container_width=True)
                st.markdown(f"**{g['name']}**")
                st.caption(f"{g['brand']}")
                usd = price_usd_with_commas(g["price"])
                ngn = convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate)
                st.write(f"**Price:** {usd} | {ngn}")

        # Build comparison DataFrame-like table (rows = key fields)
        comp_rows = {}
        for g in picked:
            comp_rows[g["name"]] = {
                "Brand": g["brand"],
                "Category": g["category"],
                "Price (USD)": price_usd_with_commas(g["price"]),
                "Price (NGN)": convert_usd_to_ngn_str(g["price"], usd_to_ngn_rate),
                "Short Specs": g["specs"]
            }
        df = pd.DataFrame(comp_rows).T
        st.markdown("### 📑 Quick Comparison Table")
        st.table(df)
        
        # Price Comparison Chart
        st.markdown("### 📊 Price Comparison")
        price_df = df[["Price (USD)"]].copy()
        # Clean price string for plotting
        price_df["Price (USD)"] = price_df["Price (USD)"].str.replace('$', '').str.replace(',', '').astype(float)
        st.bar_chart(price_df)

        # Full specs expanders for each
        st.markdown("### 🔎 Full Specs")
        for g in picked:
            with st.expander(f"{g['name']} — Full Specs"):
                fs = g.get("full_specs")
                if isinstance(fs, dict):
                    for k, v in fs.items():
                        st.write(f"- **{k}:** {v}")
                else:
                    st.write(g.get("specs", "No further specs available."))

# ----------------------------
# ABOUT
# ----------------------------
elif menu == "About":
    st.markdown('<div class="mtg-card">', unsafe_allow_html=True)
    st.title("About Mobile Tech Gist")
    st.write(
        "Mobile Tech Gist is a compact GSMArena-style demo built with Streamlit. "
        "It showcases 50+ gadgets (phones, laptops, tablets, smartwatches and headphones) "
        "with live USD→NGN pricing, images, search & compare features."
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Footer note
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="mtg-small">Built with ❤️ — prices are mid-market conversions and update hourly. Images load from public image hosts.</div>', unsafe_allow_html=True)