import qrcode
site_url = "https://YOUR-USERNAME.github.io/nnc-ingy-contact/"
qrcode.make(site_url).save("NNC_Ingy_Website_QR.png")
print("QR generated for:", site_url)
