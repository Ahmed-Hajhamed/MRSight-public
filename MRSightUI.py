from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QCheckBox, QComboBox, 
                             QLabel, QGroupBox, QGridLayout, QToolTip,
                             QTextEdit, QSplitter, QAction,
                             )
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from AboutDialog import AboutDialog
from GraphWidget import GraphWidget


class MRSightMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        # Set window properties
        self.setWindowTitle('MRSight - Weighted Visibility Graphs for MRS Analysis and Assessment')
        self.setGeometry(100, 100, 1400, 900)
        self.setWindowIcon(QIcon("Images/MRSight_Logo.png"))
        
        # Set application style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLabel {
                color: #ffffff;
                font-size: 13px;
                font-weight: bold;
            }
            QGroupBox {
                color: #ffffff;
                border: 2px solid #555;
                border-radius: 5px;
                margin-top: 10px;
                font-weight: bold;
            }
            QGroupBox {
                font-size: 16px;
                }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px 0 5px;
            }
            QPushButton {
                background-color: #8b4989;
                color: white;
                border: none;
                padding: 8px;
                border-radius: 4px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #a85aa6;
            }
            QPushButton:pressed {
                background-color: #6d3a6b;
            }
            QComboBox {
                background-color: #3c3c3c;
                color: white;
                border: 1px solid #555;
                padding: 5px;
                border-radius: 3px;
                font-size: 13px;
                font-weight: bold;
            }
            QComboBox:hover {
                border: 1px solid #8b4989;
            }
            QComboBox QAbstractItemView {
                background-color: #3c3c3c;
                color: white;
                selection-background-color: #8b4989;
                font-size: 13px;
                font-weight: bold;
            }
            QCheckBox {
                font-size: 13px;
                font-weight: bold;
                color: white;
                spacing: 5px;
                background-color: #555;
                padding: 5px;
                border-radius: 3px;
                }
            QCheckBox:hover {
                background-color: #666;
                }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox::indicator:unchecked {
                background-color: #3c3c3c;
                border: 2px solid #555;
                border-radius: 3px;
            }
            QCheckBox::indicator:checked {
                background-color: #8b4989;
                border: 2px solid #8b4989;
                border-radius: 3px;
            }
            QTextEdit {
                background-color: #1e1e1e;
                color: #aaa;
                border: 1px solid #444;
                padding: 10px;
                font-family: 'Consolas', 'Monaco', monospace;
            }
        """)
        
        # Create menu bar
        self.createMenuBar()
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        
        # Create left panel for controls
        left_panel = self.createLeftPanel()
        
        # Create right panel for visualization (placeholder)
        right_panel = self.createRightPanel()
        
        # Add panels to splitter for resizable layout
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 3)
        
        main_layout.addWidget(splitter)
        
    def createMenuBar(self):
        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background-color: #2b2b2b;
                color: white;
            }
            QMenuBar::item:selected {
                background-color: #8b4989;
            }
            QMenu {
                background-color: #3c3c3c;
                color: white;
            }
            QMenu::item:selected {
                background-color: #8b4989;
            }
        """)
        
        # Help menu
        help_menu = menubar.addMenu('Help')
        
        controls_action = QAction('Show Controls', self)
        controls_action.setShortcut('F1')
        controls_action.triggered.connect(self.showControlsHelp)
        help_menu.addAction(controls_action)
        
        about_action = QAction('About MRSight', self)
        about_action.setShortcut('F2')
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
    def createLeftPanel(self):
        left_widget = QWidget()
        left_widget.setMaximumWidth(400)
        layout = QVBoxLayout(left_widget)
        
        # Title
        title_label = QLabel('MRSight')
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #FF6CDF;
            padding: 10px;
            background-color: #1e1e1e;
            border-radius: 5px;
            margin-bottom: 10px;
        """)
        layout.addWidget(title_label)
        
        # Subject Selection Group
        subject_group = QGroupBox("Subject Selection")
        subject_layout = QVBoxLayout()
        
        # Primary Subject
        primary_layout = QHBoxLayout()
        primary_label = QLabel("Primary Subject:")
        primary_label.setMinimumWidth(100)
        self.primary_subject_combo = QComboBox()
        self.primary_subject_combo.addItems([f"Subject {i//2} (Time {i%2+1})" for i in range(18)])
        self.primary_subject_combo.setCurrentIndex(0)
        self.primary_subject_combo.currentIndexChanged.connect(self.change_subject)
        primary_layout.addWidget(primary_label)
        primary_layout.addWidget(self.primary_subject_combo)
        subject_layout.addLayout(primary_layout)
        
        # Comparison Subject
        comparison_layout = QHBoxLayout()
        self.enable_comparison_check = QCheckBox("Enable Comparison")
        self.enable_comparison_check.stateChanged.connect(self.toggleComparison)
        comparison_layout.addWidget(self.enable_comparison_check)
        subject_layout.addLayout(comparison_layout)

        
        comparison_subject_layout = QHBoxLayout()
        comparison_label = QLabel("Comparison Subject:")
        comparison_label.setMinimumWidth(100)
        self.comparison_subject_combo = QComboBox()
        self.comparison_subject_combo.addItems([f"Subject {i//2} (Time {i%2+1})" for i in range(18)])
        self.comparison_subject_combo.setCurrentIndex(2)
        self.comparison_subject_combo.currentIndexChanged.connect(self.change_comparison_subject)
        self.comparison_subject_combo.setEnabled(False)
        comparison_subject_layout.addWidget(comparison_label)
        comparison_subject_layout.addWidget(self.comparison_subject_combo)
        subject_layout.addLayout(comparison_subject_layout)
        
        subject_group.setLayout(subject_layout)
        layout.addWidget(subject_group)
        
        graph_type_group = QGroupBox("Graph Type")
        graph_type_layout = QVBoxLayout()
        graph_type_combo = QComboBox()
        graph_type_combo.addItems([
                "Complete Metabolite Graph", "Natural Visibility Graph", "Horizontal Visibility Graph"
                ])
        graph_type_combo.currentTextChanged.connect(self.change_graph_type)
        graph_type_layout.addWidget(graph_type_combo)
        graph_type_group.setLayout(graph_type_layout)
        layout.addWidget(graph_type_group)

        # Metabolites Group
        metabolites_group = QGroupBox("Metabolites")
        metabolites_layout = QVBoxLayout()
        
        # Create metabolite checkboxes in a grid
        metabolite_grid = QGridLayout()
        metabolites = [
            ('ATPα', False), ('MP', True), ('ATPβ', True), ('GPC', False),
            ('ATPγ', False), ('GPE', False), ('PCr', True), ('PC (PDE)', False),
            ('Pi', True), ('PE (PDE)', False), ('NAD+', True), ('DPG_d', False),
            ('NADH', False), ('DPG_t', False)
        ]
        self.checkboxes = {}
        for i, (metabolite, checked) in enumerate(metabolites):
            checkbox = QCheckBox(metabolite)
            checkbox.setChecked(checked)
            row = i // 2
            col = i % 2
            self.checkboxes[metabolite] = checkbox
            checkbox.toggled.connect(lambda: self.draw_graph())
            checkbox.toggled.connect(lambda: self.draw_spectrum())
                        # Add color indicator
            color_indicator = QLabel()
            color_indicator.setFixedSize(16, 16)
            color_indicator.setStyleSheet(f"background-color: {colors[metabolite]}; border-radius: 8px;")
            
            checkbox_layout = QHBoxLayout()
            checkbox_layout.addWidget(color_indicator)
            checkbox_layout.addWidget(checkbox)
            metabolite_grid.addLayout(checkbox_layout, row, col)

        metabolites_layout.addLayout(metabolite_grid)
        metabolites_group.setLayout(metabolites_layout)
        layout.addWidget(metabolites_group)
        
        meta_data_group = QGroupBox("Nodes Local Features")
        meta_data_layout = QVBoxLayout()
        self.enable_node_metadata_check = QCheckBox("Enable Node Metadata")
        meta_data_layout.addWidget(self.enable_node_metadata_check)

        meta_data_group.setLayout(meta_data_layout)
        layout.addWidget(meta_data_group)

        global_features_group = QGroupBox("Graph Global Features")
        global_features_layout = QHBoxLayout()
        # Create control instructions
        self.primary_global_features_text = QTextEdit()
        self.primary_global_features_text.setReadOnly(True)

        self.comparison_global_features_text = QTextEdit()
        self.comparison_global_features_text.setReadOnly(True)

        global_features_layout.addWidget(self.primary_global_features_text)
        global_features_layout.addWidget(self.comparison_global_features_text)

        global_features_group.setLayout(global_features_layout)
        layout.addWidget(global_features_group)

        # Add stretch to push everything to top
        layout.addStretch()
        
        return left_widget
        
    def createRightPanel(self):
        right_widget = QWidget()
        layout = QVBoxLayout(right_widget)

        self.graph_widget = GraphWidget()
        self.spectrum_widget = GraphWidget()
        self.spectrum_widget.figure.tight_layout(pad=1.5)

        self.graph_group = QGroupBox(
            f"Ratio-Weighted Complete Metabolite Graph - Subject {self.primary_subject_combo.currentIndex()//2} (Time {self.primary_subject_combo.currentIndex()%2+1})"
        )
        self.spectrum_group = QGroupBox(
            f"MRS Spectrum - Subject {self.primary_subject_combo.currentIndex()//2} (Time {self.primary_subject_combo.currentIndex()%2+1})"
        )

        graph_layout= QVBoxLayout()
        spectrum_layout = QVBoxLayout()
        graph_layout.addWidget(self.graph_widget)
        spectrum_layout.addWidget(self.spectrum_widget)

        self.graph_group.setLayout(graph_layout)
        self.spectrum_group.setLayout(spectrum_layout)
        self.spectrum_group.setMaximumHeight(300)
        layout.addWidget(self.graph_group)
        layout.addWidget(self.spectrum_group)
        
        return right_widget
        
    def toggleComparison(self, state):
        """Enable/disable comparison subject combo based on checkbox state"""
        self.comparison_subject_combo.setEnabled(state == Qt.Checked)
        self.draw_graph()


    def show_about(self):
        dlg = AboutDialog(self)
        dlg.exec_()

    def showControlsHelp(self):
        """Show a tooltip with control instructions"""
        QToolTip.showText(
            self.mapToGlobal(self.rect().center()),
            """
            <b>MRSight Controls:</b><br>
            <br>
            <b>Double-click:</b> Highlight edge or arrow<br>
            <b>Single-click:</b> Change edge direction<br>
            <b>Hover Over a Node:</b> Show its Meta data<br>
            <br>
            <b>F1:</b> Show this help
            """,
            self,
            self.rect()
        )

def style_global_features(subject_index, graph):
    styled_text = f"""
        <style>
            body {{ 
                color: #cccccc;
                font-family: 'Segoe UI', Arial, sans-serif;
                padding: 8px;
                margin: 0;
            }}
            .title {{
                color: #FF6CDF;
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 10px;
                border-bottom: 1px solid #555;
                padding-bottom: 5px;
            }}
            .metric {{
                margin: 8px 0;
                display: flex;
                justify-content: space-between;
            }}
            .key {{
                color: #FF6CDF;
                font-weight: bold;
            }}
            .value {{
                color: #fff;
                background-color: rgba(139, 73, 137, 0.2);
                padding: 2px 8px;
                border-radius: 3px;
                font-weight: bold;
            }}
        </style>
        <div class="title">Subject {subject_index//2} (Time {subject_index%2+1}) Metrics</div>
        <div class="metric"><span class="key">Global Efficiency:</span> <span class="value">{graph.global_efficiency:.3f}</span></div>
        <div class="metric"><span class="key">Path Length:</span> <span class="value">{graph.char_path_length:.3f}</span></div>
        <div class="metric"><span class="key">Transitivity:</span> <span class="value">{graph.undirected_transitivity_wu:.3f}</span></div>
        <div class="metric"><span class="key">Avg. Local Efficiency:</span> <span class="value">{graph.average_local_efficiency:.3f}</span></div>
        <div class="metric"><span class="key">Avg. Betweenness Centrality:</span> <span class="value">{graph.average_betweenness_centrality:.3f}</span></div>
    """
    return styled_text

colors = {
    "ATPα": '#FF3333',        # Bright Red
    "ATPβ": '#33FF33',        # Bright Green
    "ATPγ": '#FFFF33',        # Bright Yellow
    "PCr": '#3366FF',         # Bright Blue
    "Pi": '#FF8000',          # Bright Orange
    "NAD+": "#D370F4",        # Bright Purple
    "NADH": '#00FFFF',        # Bright Cyan
    "MP": '#FF33FF',          # Bright Magenta
    "GPC": '#CCFF00',         # Bright Lime
    "GPE": '#FF99CC',         # Bright Pink
    "PC (PDE)": '#00CC99',    # Bright Teal
    "PE (PDE)": '#BB99FF',    # Bright Lavender
    "DPG_d": '#FF9966',       # Bright Coral
    "DPG_t": '#FFB700',       # Bright Amber
}