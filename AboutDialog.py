from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QPixmap, QColor, QPalette, QLinearGradient
from PyQt5.QtCore import Qt


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About MRSight")
        self.setFixedSize(450, 500)
        
        # Set gradient background
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(240, 240, 250))
        gradient.setColorAt(1, QColor(225, 225, 240))
        
        palette = self.palette()
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        layout = QVBoxLayout()  
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setAlignment(Qt.AlignTop)

        # Logo with drop shadow effect
        logo = QLabel()
        pixmap = QPixmap("Images/MRSight_Logo.png")
        if not pixmap.isNull():
            logo.setPixmap(pixmap.scaled(120, 120, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            logo.setAlignment(Qt.AlignCenter)
            layout.addWidget(logo)

        # Tool name & version with custom font
        name_label = QLabel("<h1 style='color:#6a2c70; text-shadow: 1px 1px 2px rgba(0,0,0,0.2);'>MRSight v1.0</h1>")
        name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(name_label)

        # Divider line
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        divider.setStyleSheet("background-color: #6a2c70; margin: 5px 50px;")
        layout.addWidget(divider)

        # Short description with modern styling
        desc_label = QLabel(
            "<p align='center' style='color:#1a5e63; font-size:16px; margin: 10px;'>"
            "A visualization and analysis tool for MRS metabolite networks "
            "using advanced graph theory metrics."
            "</p>"
        )
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)

        # Credits in a styled box
        credits_frame = QFrame()
        credits_frame.setFrameShape(QFrame.StyledPanel)
        credits_frame.setStyleSheet("background-color: rgba(255,255,255,0.6); border-radius: 10px; padding: 10px;")
        credits_layout = QVBoxLayout(credits_frame)
        
        credits_label = QLabel(
            "<p align='center' style='color:#6a2c70; font-size:15px;'>"
            "<b>Developed by:</b><br>"
            "Ahmed Hajhamed<br>"
            "Ammar Yassir<br>"
            "Muhammed Ahmed<br>"
            "Ziad Wael<br>"
            "<span style='color:#1a5e63;'><b>Supervisor:</b> Prof. Mohamed Rushdi</span>"
            "</p>"
        )
        credits_label.setWordWrap(True)
        credits_layout.addWidget(credits_label)
        layout.addWidget(credits_frame)

        # Links with hover effects
        links_layout = QHBoxLayout()
        links_layout.setSpacing(20)
        
        link_style = "QLabel { color: #6a2c70; font-size: 14px; padding: 5px; border-radius: 5px; background: rgba(255,255,255,0.5); }"
        link_style += "QLabel:hover { background: rgba(255,255,255,0.8); }"
        
        doc_link = QLabel('<a style="text-decoration:none; color:#6a2c70;" href="https://drive.google.com/file/d/18ctgvdg2DPwjkpCIBVpTUZ8ihHs9mG98/view?usp=sharing">📄 Documentation</a>')
        git_link = QLabel('<a style="text-decoration:none; color:#6a2c70;" href="https://github.com/Ahmed-Hajhamed/MRSight-public">🐙 GitHub</a>')
        email_link = QLabel('<a style="text-decoration:none; color:#6a2c70;" href="mailto:ahmed.hajhamed03@eng-st.cu.edu.eg">✉️ Contact</a>')

        for link in (doc_link, git_link, email_link):
            link.setOpenExternalLinks(True)
            link.setAlignment(Qt.AlignCenter)
            link.setStyleSheet(link_style)
            links_layout.addWidget(link)
        
        layout.addLayout(links_layout)

        # Close button with styling
        button_layout = QHBoxLayout()
        close_btn = QPushButton("Close")
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #6a2c70;
                color: white;
                border-radius: 15px;
                padding: 8px 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #8e44ad;
            }
            QPushButton:pressed {
                background-color: #5a1a60;
            }
        """)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.accept)
        button_layout.addStretch()
        button_layout.addWidget(close_btn)
        button_layout.addStretch()
        layout.addLayout(button_layout)

        self.setLayout(layout)