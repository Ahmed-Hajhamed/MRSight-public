from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QVBoxLayout, QWidget

class GraphWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.figure, self.axes = plt.subplots(1, 1)

        self.figure.tight_layout(pad=0.8)

        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Remove widget margins
        layout.addWidget(self.canvas)
        self.setLayout(layout)

plot_gray_style = {
    'axes.facecolor': '2E2E2E',    # Dark gray background for axes
    'figure.facecolor': '2b2b2b',  # Dark gray background for the figure
    'axes.edgecolor': 'white',      # White edges for axes
    'axes.labelcolor': 'white',     # White labels
    'xtick.color': 'white',         # White tick marks on x-axis
    'ytick.color': 'white',         # White tick marks on y-axis
    'text.color': 'white',          # White text
    'grid.color': '#444444',        # Slightly lighter grid lines
    'grid.linestyle': '--',         # Dashed grid lines
    'lines.color': 'cyan',          # Default line color
    'patch.edgecolor': 'white',     # Edge color for patches
    'legend.facecolor': '#4C4C4C',  # Darker gray background for legends
    'legend.edgecolor': 'white',    # White edges for legends
}
plt.style.use(plot_gray_style)