import qrcode 

dato = "https://articulo.tucarro.com.co/MCO-1587895727-ford-mustang-gt-premium-2025-_JM#polycard_client=search-nordic&position=20&search_layout=grid&type=item&tracking_id=16bd78c0-6e31-48c6-89fa-186dfd6466d7"
qr = qrcode.make(dato)
qr.save("qr.png")