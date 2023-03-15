import streamlit as st

from PIL import Image
import numpy as np
import cv2



#DEMO_IMAGE = 'pavan-kunchala-QR.png'
DEMO_IMAGE = 'qr_sjc.png'

#title of the web-app
st.title('QR Code')

@st.cache_data
def show_qr_detection(img,pts):
    
    pts = np.int32(pts).reshape(-1, 2)
    
    for j in range(pts.shape[0]):
        
        cv2.line(img, tuple(pts[j]), tuple(pts[(j + 1) % pts.shape[0]]), (255, 0, 0), 5)
        
    for j in range(pts.shape[0]):
        cv2.circle(img, tuple(pts[j]), 10, (255, 0, 255), -1)


@st.cache_data
def qr_code_dec(image):
    
    decoder = cv2.QRCodeDetector()
    
    data, vertices, rectified_qr_code = decoder.detectAndDecode(image)
    
    if len(data) > 0:
        print("Decoded Data: '{}'".format(data))

    # Show the detection in the image:
        show_qr_detection(image, vertices)
        
        rectified_image = np.uint8(rectified_qr_code)
        
        decoded_data = 'Click : '+ data
        
        rectified_image = cv2.putText(rectified_image,decoded_data,(50,350),fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale = 2,
            color = (250,225,100),thickness =  3, lineType=cv2.LINE_AA)
        
        
    return decoded_data


    
    
st.markdown("**Aviso** Somente arquivos de QR-code, formatos jpg, peg e png.")


#uploading the imges
img_file_buffer = st.file_uploader("Carregar uma imagem de QR-code", type=[ "jpg", "jpeg",'png'])

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))

else:
    demo_image = DEMO_IMAGE
    image = np.array(Image.open(demo_image))


st.subheader('Image original')

#display the image
st.image(
    image, caption=f"Imagem original", use_column_width=True
) 



st.subheader('Imagem Decodificada')

#if st.button("Decodificar"):
decoded_data = qr_code_dec(image)
st.markdown(decoded_data)



    
