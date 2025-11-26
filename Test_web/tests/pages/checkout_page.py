from tests.pages.base import BasePage
import os
from utils.config import Config
import allure


class CheckoutPage(BasePage):

    #   selectores #
    url_checkout = f"{Config.url_staging}/checkout"
    nombre_completo_input = "input[name='nombre']"
    email_input = "input[name='correo']"
    telefono_input = "input[name='telefono']"
    direccion_input = "input[name='direccion']"
    ciudad_input = "input[name='ciudad']"
    comuna_input = "input[name='comuna']"
    metodo_pago_select = "xpath=//*[@id='checkout-form']/div[3]/div[2]/div/label"
    realizar_pedido_btn = "button#realizar-pedido"
    mensaje_confirmacion = "#swal2-title"
    mensaje_error = "div.error-message"
    campo_obligatorio_error = "span.campo-obligatorio"
    email_invalido_error = "span.email-invalido"
    telefono_invalido_error = "span.telefono-invalido"
    titulo_checkout = "head > title"
    qr_flow_img = "#qr-img"
    div_qr_flow = "#qr-flow-container"
    boton_cancelar_flow = "#cancel-btn"
    boton_confirmar_cancelacion = (
        "body > div > div > div.swal2-actions > button.swal2-confirm.swal2-styled"
    )

    def ir_a_checkout(self):
        self.ir_a(self.url_checkout)

    def completar_formulario_checkout(self):
        self.escribir(self.email_input, "skillsofdeath@gmail.com")
        self.escribir(self.telefono_input, "123456789")
        self.escribir(self.nombre_completo_input, "Homero J. Simpson")
        self.escribir(self.direccion_input, "Calle Falsa 123")
        self.escribir(self.ciudad_input, "Springfield")
        self.escribir(self.comuna_input, "springfield")

    def return_titulo_checkout(self):
        return self.obtener_titulo()

    def validar_generacion_qr(self):
        self.esperar_elemento(self.div_qr_flow, timeout=5000)
        return self.esta_visible(self.qr_flow_img)

    def seleccionar_flow(self):
        return self.hacer_click(self.metodo_pago_select)

    def cancelar_flow(self):
        return self.hacer_click(self.boton_cancelar_flow)

    def Mensaje_confirmacion(self):
        return self.obtener_mensaje(self.mensaje_confirmacion)

    def confirmar_cancelacion(self):
        self.esperar_elemento(self.boton_confirmar_cancelacion)
        self.hacer_click(self.boton_confirmar_cancelacion)

    def mensaje_confirmacion_cancelacion(self):
        mensaje = self.obtener_heading_sweetAlert()
        return mensaje
