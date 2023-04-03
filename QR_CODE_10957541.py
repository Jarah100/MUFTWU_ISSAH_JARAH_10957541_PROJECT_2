
import PySimpleGUI as sg
import qrcode 
import os


layout =[
        
        [sg.Text('Enter a Link,Text or Website to Generate a QR CODE ',text_color='Black',justification='center')],
        [sg.Input(key='WEB')],
        [sg.Button('CREATE QR CODE',key='CREATE QR CODE')],
        [sg.Image(key='Image', size=(50, 50))],
        
        [sg.Button('CLOSE',key='close')],
        
           
         ]

        
window=sg.Window('QR CODE GENERATOR APP', layout)

def generate_qr_code(link):
        qr=qrcode.QRCode(
                version=1,
                box_size=10,
                border=10
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill='black',back_color='white')
        file_name= 'qr_code' + '.png'
        path= os.path.join(os.getcwd(), file_name)
        img.save(path)
        return path


while True:
       event,values=window.read()
       if event==sg.WIN_CLOSED or event== 'close':
               break
       if event== 'CREATE QR CODE':
               WEB= values['WEB']
               qr_code_image_path= generate_qr_code(WEB)
               window['Image'].update(filename=qr_code_image_path)


        
window.close()