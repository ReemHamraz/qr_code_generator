import qrcode
import os


def generate_qr():
    print("=====QR Code Generator=====")
    url= input("Enter the URL:").strip()

    if not url:
        print("Error: No url entered")
        return


    file_path= input("\nEnter full save path including filename (e.g. C:/Users/You/Desktop/qr.png): ").strip()

    if not file_path.lower().endswith(".png"):
        file_path += ".png"

    directory = os.path.dirname(file_path)

    # Check if folder exists
    if directory and not os.path.exists(directory):
        print("\n Error: The directory does not exist.")
        print("Make sure the folder path is correct.")
        return
    
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_path)

        print(f"\n QR Code saved successfully at:\n{file_path}")

    except PermissionError:
        print("\n Permission denied.")
        print("You attempted to save to a restricted location.\nTry saving to Desktop or Documents.")

    except Exception as e:
        print("\nUnexpected error:", e)


if __name__== "__main__":
    generate_qr()


