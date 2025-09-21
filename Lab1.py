# Importar esta babosada del PyQt5
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
import sys

# Función que hace la magia, como dijo un sabio alguna vez (yo)
def CalcularBalance():
    try:
        # Sacamos la plata que la persona dice que gana
        ingresos = float(CampoIngresos.text())
        gastos = float(CampoGastos.text())
        
        # Calculamos el balance: lo que entra - lo que se va
        balance = ingresos - gastos
        
        EtiquetaResultado.setText(f"Balance: {balance:.2f} $")
        
        # Decimos cómo anda la billetera del usuario
        if balance > 0:
            mensaje = "Tienes ahorro (felicidades, hoy sí llegas a fin de mes )"
        elif balance == 0:
            mensaje = "Estás equilibrado (ni fu ni fa )"
        else:
            mensaje = "Estás en déficit  (no se llega a fin de mes)"
        
        EtiquetaEstado.setText(mensaje)

        # Mostramos un mensajito emergente corto y bonito
        QMessageBox.information(ventana, "Estado financiero", mensaje)

    except ValueError:
        EtiquetaResultado.setText("Por favor ingrese solo números válidos ")
        EtiquetaEstado.setText("")
        QMessageBox.warning(ventana, "Error", "Ups... solo se aceptan números ")


app = QApplication(sys.argv)
ventana = QWidget()
ventana.setWindowTitle("Calculadora de Gastos Personales")
ventana.setGeometry(100, 100, 400, 300)

# Usaremos un layout vertical porque somos simples y no complicados
layout = QVBoxLayout()

# Widgets (las piezas del rompecabezas visual)
EtiquetaTitulo = QLabel("Calculadora de Gastos Personales")
EtiquetaIngresos = QLabel("Ingrese sus ingresos:")
CampoIngresos = QLineEdit()

EtiquetaGastos = QLabel("Ingrese sus gastos:")
CampoGastos = QLineEdit()

BotonCalcular = QPushButton("Calcular Balance")
EtiquetaResultado = QLabel("Aquí aparecerá tu balance...")
EtiquetaEstado = QLabel("Aquí aparecerá tu estado financiero...")

# Conectar el botón con la función
BotonCalcular.clicked.connect(CalcularBalance)

layout.addWidget(EtiquetaTitulo)
layout.addWidget(EtiquetaIngresos)
layout.addWidget(CampoIngresos)
layout.addWidget(EtiquetaGastos)
layout.addWidget(CampoGastos)
layout.addWidget(BotonCalcular)
layout.addWidget(EtiquetaResultado)
layout.addWidget(EtiquetaEstado)

ventana.setLayout(layout)

# Mostrar la ventana
ventana.show()
sys.exit(app.exec_())
