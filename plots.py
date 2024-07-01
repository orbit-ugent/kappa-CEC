import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import plotly.graph_objects as go

def plot1(fig1, ax1, ax2, ax3, ax4, ax5, ax6):
    fig1.tight_layout()

    #ax1.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax1.tick_params(axis='y', labelsize=12) 
    ax1.tick_params(axis='x', labelsize=12) 
    #ax1.set_xlabel('Clay [%]', fontsize = 16) 
    ax1.set_ylabel('Klf_IP [m-3] all', fontsize = 16) 
    ax1.grid(True) 
    ax1.set_xlim(0, 80) 

    #ax2.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax2.tick_params(axis='y', labelsize=12) 
    ax2.tick_params(axis='x', labelsize=12) 
    #ax2.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax2.set_ylabel('Klf [m3/kg]', fontsize = 16) 
    ax2.grid(True) 
    ax2.set_xlim(0, 45) 

    #ax3.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax3.tick_params(axis='y', labelsize=12) 
    ax3.tick_params(axis='x', labelsize=12) 
    #ax3.set_xlabel('Clay [%]', fontsize = 16) 
    ax3.set_ylabel('Klf_IP [m-3] arch', fontsize = 16) 
    ax3.grid(True) 
    ax3.set_xlim(0, 80) 

    #ax4.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax4.tick_params(axis='y', labelsize=12) 
    ax4.tick_params(axis='x', labelsize=12) 
    #ax4.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax4.set_ylabel('Klf [m3/kg]', fontsize = 16) 
    ax4.grid(True) 
    ax4.set_xlim(0, 45) 

    #ax5.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax5.tick_params(axis='y', labelsize=12) 
    ax5.tick_params(axis='x', labelsize=12) 
    ax5.set_xlabel('Clay [%]', fontsize = 16) 
    ax5.set_ylabel('Klf_IP [m-3] no arch', fontsize = 16) 
    ax5.grid(True) 
    ax5.set_xlim(0, 80) 

    #ax6.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax6.tick_params(axis='y', labelsize=12) 
    ax6.tick_params(axis='x', labelsize=12) 
    ax6.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax6.set_ylabel('Klf [m3/kg]', fontsize = 16) 
    ax6.grid(True) 
    ax6.set_xlim(0, 45) 


def plot2(fig2, ax1, ax2, ax3, ax4, ax5, ax6):
    fig2.tight_layout()

    #ax1.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax1.tick_params(axis='y', labelsize=12) 
    ax1.tick_params(axis='x', labelsize=12) 
    #ax1.set_xlabel('Clay [%]', fontsize = 16) 
    ax1.set_ylabel('Kfd_abs [m3/kg] all', fontsize = 16) 
    ax1.grid(True) 
    ax1.set_xlim(0, 80) 

    #ax2.legend(loc='upper right', fontsize = 8)
    #ax2.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax2.tick_params(axis='y', labelsize=12) 
    ax2.tick_params(axis='x', labelsize=12) 
    #ax2.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax2.set_ylabel('Kfd_abs [m3/kg]', fontsize = 16) 
    ax2.grid(True) 
    ax2.set_xlim(0, 45) 

    #ax3.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax3.tick_params(axis='y', labelsize=12) 
    ax3.tick_params(axis='x', labelsize=12) 
    #ax3.set_xlabel('Clay [%]', fontsize = 16) 
    ax3.set_ylabel('Kfd_abs [m3/kg] arch', fontsize = 16) 
    ax3.grid(True) 
    ax3.set_xlim(0, 80) 

    #ax4.legend(loc='upper right', fontsize = 8)
    #ax4.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax4.tick_params(axis='y', labelsize=12) 
    ax4.tick_params(axis='x', labelsize=12) 
    #ax4.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax4.set_ylabel('Kfd_abs [m3/kg]', fontsize = 16) 
    ax4.grid(True) 
    ax4.set_xlim(0, 45) 

    #ax5.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax5.tick_params(axis='y', labelsize=12) 
    ax5.tick_params(axis='x', labelsize=12) 
    ax5.set_xlabel('Clay [%]', fontsize = 16) 
    ax5.set_ylabel('Kfd_abs [m3/kg] no arch', fontsize = 16) 
    ax5.grid(True) 
    ax5.set_xlim(0, 80) 

    #ax6.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax6.tick_params(axis='y', labelsize=12) 
    ax6.tick_params(axis='x', labelsize=12) 
    ax6.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax6.set_ylabel('Kfd_abs [m3/kg]', fontsize = 16) 
    ax6.grid(True) 
    ax6.set_xlim(0, 45) 


def plot3(fig3, ax1, ax2, ax3, ax4, ax5, ax6):
    fig3.tight_layout()

    ax1.legend(loc='upper right', fontsize = 8)
    #ax1.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax1.tick_params(axis='y', labelsize=12) 
    ax1.tick_params(axis='x', labelsize=12) 
    #ax1.set_xlabel('Clay [%]', fontsize = 16) 
    ax1.set_ylabel('Kfd [%] all', fontsize = 16) 
    ax1.grid(True) 
    ax1.set_ylim(0, 5e-3)  
    ax1.set_xlim(0, 80) 
    ax1.legend(loc='upper right', fontsize = 10)

    #ax2.legend(loc='upper right', fontsize = 8)
    #ax2.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax2.tick_params(axis='y', labelsize=12) 
    ax2.tick_params(axis='x', labelsize=12) 
    #ax2.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax2.set_ylabel('Kfd [%]', fontsize = 16) 
    ax2.grid(True) 
    ax2.set_ylim(0, 5e-3)  
    ax2.set_xlim(0, 45) 
    ax2.legend(loc='upper right', fontsize = 10)

    ax3.legend(loc='upper right', fontsize = 8)
    #ax3.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax3.tick_params(axis='y', labelsize=12) 
    ax3.tick_params(axis='x', labelsize=12) 
    #ax3.set_xlabel('Clay [%]', fontsize = 16) 
    ax3.set_ylabel('Kfd [%] arch', fontsize = 16) 
    ax3.grid(True) 
    ax3.set_ylim(0, 5e-3)  
    ax3.set_xlim(0, 80) 
    ax3.legend(loc='upper right', fontsize = 10)

    #ax4.legend(loc='upper right', fontsize = 8)
    #ax4.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax4.tick_params(axis='y', labelsize=12) 
    ax4.tick_params(axis='x', labelsize=12) 
    #ax4.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax4.set_ylabel('Kfd [%]', fontsize = 16) 
    ax4.grid(True) 
    ax4.set_ylim(0, 5e-3)  
    ax4.set_xlim(0, 45) 
    ax4.legend(loc='upper right', fontsize = 10)

    #ax5.legend(loc='upper right', fontsize = 8)
    #ax5.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax5.tick_params(axis='y', labelsize=12) 
    ax5.tick_params(axis='x', labelsize=12) 
    ax5.set_xlabel('Clay [%]', fontsize = 16) 
    ax5.set_ylabel('Kfd [%] no arch', fontsize = 16) 
    ax5.grid(True) 
    ax5.set_ylim(0, 5e-3)  
    ax5.set_xlim(0, 80) 
    ax5.legend(loc='upper right', fontsize = 10)

    #ax6.legend(loc='upper right', fontsize = 8)
    #ax6.set_title("Susceptibility vs clay" , fontweight='bold', fontsize=20) 
    ax6.tick_params(axis='y', labelsize=12) 
    ax6.tick_params(axis='x', labelsize=12) 
    ax6.set_xlabel('CEC [meq/100g]', fontsize = 16) 
    #ax6.set_ylabel('Kfd [%]', fontsize = 16) 
    ax6.grid(True) 
    ax6.set_ylim(0, 5e-3)  
    ax6.set_xlim(0, 45) 
    ax6.legend(loc='upper right', fontsize = 10)


def ThreeD1(axa, plt):
    plt.rcParams["figure.figsize"] = (6,4) 
    plt.rcParams["figure.dpi"] = 150
    axa.tick_params(axis='y', labelsize=10) 
    axa.tick_params(axis='x', labelsize=10) 
    axa.set_xlabel(" Clay" , fontweight='bold', fontsize=12) 
    axa.set_ylabel(" F1mass" , fontweight='bold', fontsize=12) 
    axa.set_zlabel(" CEC [meq/100g]" , fontweight='bold', fontsize=12) 
    axa.set_title("  " , fontweight='bold', fontsize=16) 
    axa.set_zlim(0, 80) 


def valthe(ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, plt):
    import numpy as np
    ax1.legend(loc='lower right', fontsize = 12)
    ax1.set_title(" " , fontweight='bold', fontsize=25) 
    ax1.tick_params(axis='y', labelsize=18) 
    ax1.tick_params(axis='x', labelsize=18) 
    ax1.set_xlabel('Volumetric content [%]', fontsize = 18) 
    ax1.set_ylabel('Depth [cm]', fontsize = 18) 
    #ax1.set_yticks(np.arange(0, -120, -3))
    ax1.set_xticks(np.arange(1, 60, 5))
    ax1.grid(True) 
    #ax1.set_ylim(0, yc)  
    ax1.set_xlim(0, 60) 

    ax2.legend(loc='lower left', fontsize = 12) 
    ax2.set_title(" " , fontweight='bold', fontsize=25) 
    ax2.tick_params(axis='y', labelsize=18) 
    ax2.tick_params(axis='x', labelsize=18) 
    #ax2.set_ylabel('Depth [cm]', fontsize = 16) 
    ax2.set_xlabel('Original Bulk EC [mS/m]', fontsize = 18) 
    ax2.grid(True) 
    #ax2.set_ylim(0, yc) 
    ax2.set_xlim(0, 1.6)

    ax3.legend(loc='upper right', fontsize = 12) 
    ax3.set_title(" " , fontweight='bold', fontsize=25) 
    ax3.tick_params(axis='y', labelsize=18) 
    ax3.tick_params(axis='x', labelsize=18) 
    ax3.set_ylabel('Depth [cm]', fontsize = 18) 
    ax3.set_xlabel('Real Relative Permittivity [-]', fontsize = 18) 
    ax3.grid(True) 
    #ax3.set_ylim(0, yc) 
    ax3.set_xlim(0, 20)

    ax4.legend(loc='upper right', fontsize = 12) 
    ax4.set_title(" " , fontweight='bold', fontsize=25) 
    ax4.tick_params(axis='y', labelsize=18) 
    ax4.tick_params(axis='x', labelsize=18) 
    #ax4.set_ylabel('Depth [cm]', fontsize = 16) 
    ax4.set_xlabel('Corrected Bulk EC [mS/m]', fontsize = 18) 
    ax4.grid(True) 
    #ax4.set_ylim(0, yc) 
    ax4.set_xlim(0, 1.6)

    ax6.legend(loc='upper left', fontsize = 12) 
    ax6.set_title(" " , fontweight='bold', fontsize=25) 
    ax6.tick_params(axis='y', labelsize=18) 
    ax6.tick_params(axis='x', labelsize=18) 
    #ax6.set_ylabel('Depth [cm]', fontsize = 16) 
    ax6.set_xlabel('Water Conductivity [S/m]', fontsize = 18) 
    ax6.grid(True) 
    #ax6.set_ylim(-80, 0) 
    ax6.set_xlim(0, 0.22)
    #ax6.set_yticks(np.arange(0, 0.25, 0.02))
    ax6.set_xticks(np.arange(0, 0.22, 0.02))

    ax5.legend(loc='lower right', fontsize = 12) 
    ax5.set_title(" " , fontweight='bold', fontsize=25) 
    ax5.tick_params(axis='y', labelsize=18) 
    ax5.tick_params(axis='x', labelsize=18) 
    ax5.set_ylabel('Depth', fontsize = 16) 
    ax5.set_xlabel('Magnetic suceptibility [SI$*10^{-3}$]', fontsize = 18) 
    ax5.grid(True) 
    #ax5.set_ylim(0, 35) 
    ax5.set_xlim(0, 0.25)
    
    ax7.legend(loc='upper left', fontsize = 12) 
    #ax7.set_title("Field calibration curve " , fontweight='bold', fontsize=25) 
    ax7.tick_params(axis='y', labelsize=18) 
    ax7.tick_params(axis='x', labelsize=18) 
    ax7.set_xlabel('Real Rel. Permittivity', fontsize = 16) 
    ax7.set_ylabel('Volumetric water contect [m3/m3]', fontsize = 18) 
    ax7.grid(True) 
    ax7.set_xlim(0.001, 40) 
    ax7.set_ylim(5, 45)
    #ax7.set_yticks(np.arange(0, 0.25, 0.02))
    #ax7.set_xticks(np.arange(0, 0.22, 0.02))

    ax8.legend(loc='lower right', fontsize = 12) 
    #ax8.set_title("Field calibration curve " , fontweight='bold', fontsize=25) 
    ax8.tick_params(axis='y', labelsize=18) 
    ax8.tick_params(axis='x', labelsize=18) 
    ax8.set_xlabel('Real Rel. Permittivity', fontsize = 16) 
    ax8.set_ylabel('Volumetric water contect [m3/m3]', fontsize = 18) 
    ax8.grid(True) 
    #ax8.set_xlim(0.001, 40) 
    #ax8.set_ylim(5, 45)
    #ax8.set_yticks(np.arange(0, 0.25, 0.02))
    #ax8.set_xticks(np.arange(0, 0.22, 0.02))
    
    
def fielworkgraph(ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, plt):
    import numpy as np
    ax1.legend(loc='upper left', fontsize = 8)
    ax1.set_title(" " , fontweight='bold', fontsize=25) 
    ax1.tick_params(axis='y', labelsize=18) 
    ax1.tick_params(axis='x', labelsize=18) 
    ax1.set_xlabel('Volumetric content [%]', fontsize = 18) 
    ax1.set_ylabel('Depth [cm]', fontsize = 18) 
    #ax1.set_yticks(np.arange(0, -120, -3))
    ax1.set_xticks(np.arange(0, 60, 5))
    ax1.grid(True) 
    #ax1.set_ylim(0, yc)  
    ax1.set_xlim(0, 60) 

    ax2.legend(loc='upper right', fontsize = 8) 
    ax2.set_title(" " , fontweight='bold', fontsize=25) 
    ax2.tick_params(axis='y', labelsize=18) 
    ax2.tick_params(axis='x', labelsize=18) 
    #ax2.set_ylabel('Depth [cm]', fontsize = 16) 
    ax2.set_xlabel('Original Bulk EC [mS/m]', fontsize = 18) 
    ax2.grid(True) 
    #ax2.set_ylim(0, yc) 
    ax2.set_xlim(0, 70)

    ax3.legend(loc='upper right', fontsize = 14) 
    ax3.set_title(" " , fontweight='bold', fontsize=25) 
    ax3.tick_params(axis='y', labelsize=18) 
    ax3.tick_params(axis='x', labelsize=18) 
    ax3.set_ylabel('Depth [cm]', fontsize = 18) 
    ax3.set_xlabel('Real Relative Permittivity [-]', fontsize = 18) 
    ax3.grid(True) 
    #ax3.set_ylim(0, yc) 
    ax3.set_xlim(0, 35)

    ax4.legend(loc='upper right', fontsize = 8) 
    ax4.set_title(" " , fontweight='bold', fontsize=25) 
    ax4.tick_params(axis='y', labelsize=18) 
    ax4.tick_params(axis='x', labelsize=18) 
    #ax4.set_ylabel('Depth [cm]', fontsize = 16) 
    ax4.set_xlabel('Corrected Bulk EC [mS/m]', fontsize = 18) 
    ax4.grid(True) 
    #ax4.set_ylim(0, yc) 
    ax4.set_xlim(0, 70)

    ax5.legend(loc='upper left', fontsize = 8) 
    ax5.set_title(" " , fontweight='bold', fontsize=25) 
    ax5.tick_params(axis='y', labelsize=18) 
    ax5.tick_params(axis='x', labelsize=18) 
    #ax5.set_ylabel('Depth [cm]', fontsize = 16) 
    ax5.set_xlabel('Water Conductivity [S/m]', fontsize = 18) 
    ax5.grid(True) 
    #ax5.set_ylim(-80, 0) 
    ax5.set_xlim(0, 0.22)
    #ax5.set_yticks(np.arange(0, 0.25, 0.02))
    ax5.set_xticks(np.arange(0, 0.22, 0.02))

    ax6.legend(loc='upper left', fontsize = 8) 
    ax6.set_title(" " , fontweight='bold', fontsize=25) 
    ax6.tick_params(axis='y', labelsize=18) 
    ax6.tick_params(axis='x', labelsize=18) 
    ax6.set_ylabel('Real Permitivitty [-]', fontsize = 16) 
    ax6.set_xlabel('Correctec Bulk Conductivity [mS/m]', fontsize = 18) 
    ax6.grid(True) 
    ax6.set_ylim(0, 35) 
    ax6.set_xlim(0, 50)
    
    ax7.legend(loc='upper left', fontsize = 8) 
    #ax7.set_title("Field calibration curve " , fontweight='bold', fontsize=25) 
    ax7.tick_params(axis='y', labelsize=18) 
    ax7.tick_params(axis='x', labelsize=18) 
    ax7.set_ylabel('Real Rel. Permittivity', fontsize = 16) 
    ax7.set_xlabel('Volumetric water contect [m3/m3]', fontsize = 18) 
    ax7.grid(True) 
    ax7.set_xlim(0.00, 70) 
    ax7.set_ylim(5, 90)
    #ax7.set_yticks(np.arange(0, 0.25, 0.02))
    #ax7.set_xticks(np.arange(0, 0.22, 0.02))

    ax8.legend(loc='lower right', fontsize = 8) 
    #ax8.set_title("Field calibration curve " , fontweight='bold', fontsize=25) 
    ax8.tick_params(axis='y', labelsize=18) 
    ax8.tick_params(axis='x', labelsize=18) 
    ax8.set_ylabel('Real Rel. Permittivity', fontsize = 16) 
    ax8.set_xlabel('Volumetric water contect [m3/m3]', fontsize = 18) 
    ax8.grid(True) 
    #ax8.set_xlim(0.001, 40) 
    #ax8.set_ylim(5, 45)
    #ax8.set_yticks(np.arange(0, 0.25, 0.02))
    #ax8.set_xticks(np.arange(0, 0.22, 0.02))

def moist_curve(axa, axb, axc, axd, axe, axf, axg, axh, plt):
    import numpy as np
    xlim = 50
    axa.legend(loc='upper left', fontsize = 14)
    axa.set_title("Water content vs Real Permittivity " , fontweight='bold', fontsize=25) 
    axa.tick_params(axis='y', labelsize=20) 
    axa.tick_params(axis='x', labelsize=20) 
    axa.set_xlabel('Volumetric water content [%]', fontsize = 22) 
    axa.set_ylabel('Real Permittivity', fontsize = 22) 
    axa.set_yticks(np.arange(0, 50, 5))
    axa.set_xticks(np.arange(0, xlim, 5))
    axa.grid(True) 
    axa.set_ylim(0, 50)  
    axa.set_xlim(0, xlim) 

    axb.legend(loc='upper left', fontsize = 14)
    axb.set_title("Water content vs Im. Permittivity " , fontweight='bold', fontsize=25) 
    axb.tick_params(axis='y', labelsize=20) 
    axb.tick_params(axis='x', labelsize=20) 
    axb.set_xlabel('Volumetric water content [%]', fontsize = 22) 
    axb.set_ylabel('Imaginary Permittivity', fontsize = 22) 
    axb.set_yticks(np.arange(0, 80, 10))
    axb.set_xticks(np.arange(0, xlim, 5))
    axb.grid(True) 
    axb.set_ylim(0, 80)  
    axb.set_xlim(0, xlim) 

    axc.legend(loc='upper left', fontsize = 14)
    axc.set_title("Water content vs EC" , fontweight='bold', fontsize=25) 
    axc.tick_params(axis='y', labelsize=20) 
    axc.tick_params(axis='x', labelsize=20) 
    axc.set_xlabel('Volumetric water content [%]', fontsize = 22) 
    axc.set_ylabel('EC [mS/m]', fontsize = 22) 
    axc.set_yticks(np.arange(0, 500, 50))
    axc.set_xticks(np.arange(0, xlim, 5))
    axc.grid(True) 
    axc.set_ylim(0, 500)  
    axc.set_xlim(0, xlim) 

    axd.legend(loc='upper left', fontsize = 14)
    axd.set_title("Water content vs EC" , fontweight='bold', fontsize=25) 
    axd.tick_params(axis='y', labelsize=20) 
    axd.tick_params(axis='x', labelsize=20) 
    axd.set_xlabel('Volumetric water content [%]', fontsize = 22) 
    axd.set_ylabel('EC [mS/m]', fontsize = 22) 
    axd.set_yticks(np.arange(0, 85, 10))
    axd.set_xticks(np.arange(0, xlim, 5))
    axd.grid(True) 
    axd.set_ylim(0, 85)  
    axd.set_xlim(0, xlim) 
    
    axe.legend(loc='upper left', fontsize = 14)
    axe.set_title("Water content vs Relaxation component " , fontweight='bold', fontsize=25) 
    axe.tick_params(axis='y', labelsize=20) 
    axe.tick_params(axis='x', labelsize=20) 
    axe.set_xlabel('Volumetric water content [%]', fontsize = 22) 
    axe.set_ylabel('Relaxation component [-]', fontsize = 22) 
    #axe.set_yticks(np.arange(0, 55, 5))
    axe.set_xticks(np.arange(0, xlim, 5))
    axe.grid(True) 
    #axe.set_ylim(0, 55)  
    axe.set_xlim(0, xlim) 
    
    axf.legend(loc='lower right', fontsize = 14)
    axf.set_title("EC vs Real permittivity" , fontweight='bold', fontsize=25) 
    axf.tick_params(axis='y', labelsize=18) 
    axf.tick_params(axis='x', labelsize=18) 
    axf.set_xlabel('EC [mS/m]', fontsize = 18) 
    axf.set_ylabel('Real Permittivity', fontsize = 18) 
    axf.set_yticks(np.arange(0, 50, 5))
    #axf.set_xticks(np.arange(0, 50, 5))
    axf.grid(True) 
    axf.set_ylim(0, 50)  
    #axf.set_xlim(0, 50) 
    
    axg.legend(loc='upper left', fontsize = 14)
    axg.set_title("Water content vs Real Permittivity " , fontweight='bold', fontsize=25) 
    axg.tick_params(axis='y', labelsize=18) 
    axg.tick_params(axis='x', labelsize=18) 
    axg.set_xlabel('Volumetric water content [%]', fontsize = 18) 
    axg.set_ylabel('Real Permittivity', fontsize = 18) 
    #axg.set_yticks(np.arange(0, 300, 20))
    axg.set_xticks(np.arange(0, 50, 5))
    axg.grid(True) 
    #axg.set_ylim(0, 80)  
    axg.set_xlim(0, 50) 
    
    #axh.legend(loc='upper left', fontsize = 14)
    #axh.set_title("Water content vs Real Permittivity " , fontweight='bold', fontsize=25) 
    #axh.tick_params(axis='y', labelsize=18) 
    #axh.tick_params(axis='x', labelsize=18) 
    #axh.set_xlabel('Volumetric water content [%]', fontsize = 18) 
    #axh.set_ylabel('Real Permittivity', fontsize = 18) 
    #axh.set_yticks(np.arange(0, 50, 5))
    #axh.set_xticks(np.arange(0, 50, 5))
    #axh.grid(True) 
    #axh.set_ylim(0, 50)  
    #axh.set_xlim(0, 50) 


def pltmsc(ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, lw, yc, plt):
    ax1.legend(loc='upper right', fontsize = 10)
    ax1.set_title("Susceptibility vs Sand" , fontweight='bold', fontsize=25) 
    ax1.tick_params(axis='y', labelsize=12) 
    ax1.tick_params(axis='x', labelsize=12) 
    ax1.set_xlabel('Sand [%]', fontsize = 16) 
    ax1.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax1.grid(True) 
    ax1.set_ylim(0, yc)  
    #ax1.set_xlim(1, 50) 
    ax1.legend(loc='upper right', fontsize = 10)

    ax2.legend(loc='upper left', fontsize = 10) 
    ax2.set_title("Susceptibility vs Organic matter" , fontweight='bold', fontsize=25) 
    ax2.tick_params(axis='y', labelsize=12) 
    ax2.tick_params(axis='x', labelsize=12) 
    ax2.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax2.set_xlabel('Organic matter [%]', fontsize = 16) 
    ax2.grid(True) 
    ax2.set_ylim(0, yc) 
    #ax2.set_xlim(10, 100000)
    ax2.legend(loc='upper left', fontsize = 10) 

    ax3.grid(True) 
    ax3.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax3.set_xlabel("Cobalt [mg/Kg]" , fontsize = 16) 
    ax3.legend(loc='upper left', fontsize = 10) 
    ax3.set_title("Susceptibility vs Cobalt" , fontweight='bold', fontsize=25) 
    ax3.tick_params(axis='y', labelsize=12) 
    ax3.tick_params(axis='x', labelsize=12) 
    ax3.set_ylim(0, yc) 
    #ax3.set_xlim(0, 60) 
    ax3.legend(loc='upper left', fontsize = 10) 

    ax12.legend(loc='upper right', fontsize = 10) 
    ax12.set_title("Susceptibility vs Copper" , fontweight='bold', fontsize=25) 
    ax12.tick_params(axis='y', labelsize=12) 
    ax12.tick_params(axis='x', labelsize=12) 
    ax12.set_xlabel('Copper [mg/Kg]', fontsize = 16) 
    ax12.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax12.grid(True) 
    ax12.set_ylim(0, yc) 
    #ax12.set_xlim(0.1, 0.8) 
    ax12.legend(loc='upper right', fontsize = 10) 

    ax5.legend(loc='upper right', fontsize = 10) 
    ax5.set_title("Susceptibility vs Iron" , fontweight='bold', fontsize=25) 
    ax5.tick_params(axis='y', labelsize=12) 
    ax5.tick_params(axis='x', labelsize=12) 
    ax5.set_xlabel('Iron [mg/Kg]', fontsize = 16) 
    ax5.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax5.grid(True) 
    ax5.set_ylim(0, yc) 
    #ax5.set_xlim(0, 25) 
    ax5.legend(loc='upper right', fontsize = 10) 

    ax6.set_title("Susceptibility vs Zinc" , fontweight='bold', fontsize=25) 
    ax6.tick_params(axis='y', labelsize=12) 
    ax6.tick_params(axis='x', labelsize=12) 
    ax6.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax6.set_xlabel('Zinc [mg/Kg]', fontsize = 16) 
    ax6.grid(True) 
    #ax6.set_xlim(0, 65) 
    ax6.set_ylim(0, yc)
    ax6.legend(loc='upper right', fontsize = 10) 
    
    ax7.set_title("Susceptibility vs pH" , fontweight='bold', fontsize=25) 
    ax7.tick_params(axis='y', labelsize=12) 
    ax7.tick_params(axis='x', labelsize=12) 
    ax7.set_xlabel('pH', fontsize = 16) 
    ax7.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax7.grid(True) 
    ax7.set_ylim(0, yc) 
    #ax7.set_xlim(0, 25) 
    ax7.legend(loc='upper right', fontsize = 10) 

    ax8.set_title("LF Susceptibility vs PLI" , fontweight='bold', fontsize=25) 
    ax8.tick_params(axis='y', labelsize=12) 
    ax8.tick_params(axis='x', labelsize=12) 
    ax8.set_ylabel('LF Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax8.set_xlabel("Pollution Load Index", fontsize = 16) 
    ax8.grid(True) 
    #ax8.set_xlim(0, 65) 
    #ax8.set_ylim(0, yc)
    ax8.legend(loc='upper right', fontsize = 10) 
    
    ax9.legend(loc='upper right', fontsize = 10) 
    ax9.set_title("Susceptibility vs Chrome" , fontweight='bold', fontsize=25) 
    ax9.tick_params(axis='y', labelsize=12) 
    ax9.tick_params(axis='x', labelsize=12) 
    ax9.set_xlabel('Chrome [mg/Kg]', fontsize = 16) 
    ax9.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax9.grid(True) 
    ax9.set_ylim(0, yc) 
    #ax9.set_xlim(0, 25) 
    ax9.legend(loc='upper right', fontsize = 10) 

    ax10.set_title("Susceptibility vs Plumb" , fontweight='bold', fontsize=25) 
    ax10.tick_params(axis='y', labelsize=12) 
    ax10.tick_params(axis='x', labelsize=12) 
    ax10.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax10.set_xlabel('Plumb [mg/Kg]', fontsize = 16) 
    ax10.grid(True) 
    #ax10.set_xlim(0, 65) 
    ax10.set_ylim(0, yc)
    ax10.legend(loc='upper right', fontsize = 10) 
    
    ax11.set_title("Susceptibility vs Nickel" , fontweight='bold', fontsize=25) 
    ax11.tick_params(axis='y', labelsize=12) 
    ax11.tick_params(axis='x', labelsize=12) 
    ax11.set_xlabel('Nickel [mg/Kg]', fontsize = 16) 
    ax11.set_ylabel('Susceptibility [10−8 m3/kg]', fontsize = 16) 
    ax11.grid(True) 
    ax11.set_ylim(0, yc) 
    #ax11.set_xlim(0, 25) 
    ax11.legend(loc='upper right', fontsize = 10) 

def sets(axc1, axc2, axc3):
    wide = 90
    axc1.legend(loc='lower right', fontsize = 10)
    axc1.set_title("Field 1", fontweight='bold', fontsize=25)
    axc1.tick_params(axis='y', labelsize=12)
    axc1.tick_params(axis='x', labelsize=12)
    axc1.set_xlabel('Magnetic susceptibility [e-5]', fontweight='bold', fontsize = 16)
    axc1.set_ylabel('Depth [cm]', fontweight='bold', fontsize = 16)
    axc1.grid(True)
    #axc1.set_ylim(0, 65) 
    axc1.set_xlim(1, wide)

    axc2.legend(loc='lower right', fontsize = 10)
    axc2.set_title("Field 2", fontweight='bold', fontsize=25)
    axc2.tick_params(axis='y', labelsize=12)
    axc2.tick_params(axis='x', labelsize=12)
    axc2.set_xlabel('Magnetic susceptibility [e-5]', fontweight='bold', fontsize = 16)
    #axc2.set_ylabel('Depth [cm]', fontsize = 16)
    axc2.grid(True)
    #axc2.set_ylim(0, 65)
    axc2.set_xlim(1, wide)

    axc3.grid(True)
    axc3.set_xlabel('Magnetic susceptibility [e-5]', fontweight='bold', fontsize = 16)
    #axc3.set_ylabel('Depth [cm]', fontsize = 16)
    axc3.legend(loc='lower right', fontsize = 10)
    axc3.set_title("Field 3", fontweight='bold', fontsize=25)
    axc3.tick_params(axis='y', labelsize=12)
    axc3.tick_params(axis='x', labelsize=12)
    #axc3.set_ylim(0, 65)
    axc3.set_xlim(1, wide)
    
def camargoplots(axp1, axp2):
    axp1.legend(loc='upper right', fontsize = 10)
    axp1.set_title("Susceptibility vs Pads" , fontweight='bold', fontsize=25) 
    axp1.tick_params(axis='y', labelsize=12) 
    axp1.tick_params(axis='x', labelsize=12) 
    axp1.set_xlabel('Phosphate adsorved [mg/Kg]', fontsize = 16) 
    axp1.set_ylabel('Susceptibility [10−6 m3/kg]', fontsize = 16) 
    axp1.grid(True) 
    #axp1.set_ylim(0, yc)  
    #axp1.set_xlim(1, 50) 
    axp1.legend(loc='upper right', fontsize = 10)

    axp2.legend(loc='upper right', fontsize = 10)
    axp2.set_title("Fe vs Pads" , fontweight='bold', fontsize=25) 
    axp2.tick_params(axis='y', labelsize=12) 
    axp2.tick_params(axis='x', labelsize=12) 
    axp2.set_xlabel('Phosphate adsorved [mg/Kg]', fontsize = 16) 
    axp2.set_ylabel('Fe [mg/Kg]', fontsize = 16) 
    axp2.grid(True) 
    #axp2.set_ylim(0, yc)  
    #axp2.set_xlim(1, 50) 
    axp2.legend(loc='upper right', fontsize = 10)
    
def pltgamma(ax1, ax2, ax3, ax4, ax5, ax6, lw, yc, plt):
    
    ax1.set_title("Sand vs Th/K" , fontweight='bold', fontsize=25) 
    ax1.set_ylabel('Th / K ratio', fontsize = 16) 
    ax1.set_xlabel('Sand [%]', fontsize = 16) 
    ax1.grid(True) 
    ax1.set_ylim(0, yc)  
    #ax1.set_xlim(1, 50) 
    ax1.legend(loc='upper right', fontsize = 10)

    ax2.set_title("Silt vs Th/K" , fontweight='bold', fontsize=25) 
    ax2.set_xlabel('Silt [%]', fontsize = 16) 
    ax2.set_ylabel('Th / K ratio', fontsize = 16) 
    ax2.legend(loc='upper left', fontsize = 10) 
    ax2.tick_params(axis='y', labelsize=12) 
    ax2.tick_params(axis='x', labelsize=12) 
    ax2.grid(True) 
    ax2.set_ylim(0, yc) 
    #ax2.set_xlim(10, 100000)
    ax2.legend(loc='upper left', fontsize = 10) 

    ax3.set_xlabel('Clay [%]', fontsize = 16) 
    ax3.set_ylabel("Th / K ratio" , fontsize = 16) 
    ax3.set_title("Clay vs Th/K" , fontweight='bold', fontsize=25) 
    ax3.grid(True) 
    ax3.legend(loc='upper left', fontsize = 10) 
    ax3.tick_params(axis='y', labelsize=12) 
    ax3.tick_params(axis='x', labelsize=12) 
    ax3.set_ylim(0, yc) 
    #ax3.set_xlim(0, 60) 
    ax3.legend(loc='upper left', fontsize = 10) 

    ax4.legend(loc='upper right', fontsize = 10) 
    ax4.set_title("CEC vs Th/K" , fontweight='bold', fontsize=25) 
    ax4.tick_params(axis='y', labelsize=12) 
    ax4.tick_params(axis='x', labelsize=12) 
    ax4.set_ylabel('Th / K ratio', fontsize = 16) 
    ax4.set_xlabel('Cation Exchange Capacity [cmol/Kg]', fontsize = 16) 
    ax4.grid(True) 
    ax4.set_ylim(0, yc) 
    #ax4.set_xlim(0.1, 0.8) 
    ax4.legend(loc='upper right', fontsize = 10) 

    ax5.legend(loc='upper right', fontsize = 10) 
    ax5.set_title("pH vs Th/K" , fontweight='bold', fontsize=25) 
    ax5.tick_params(axis='y', labelsize=12) 
    ax5.tick_params(axis='x', labelsize=12) 
    ax5.set_ylabel('Th / K ratio', fontsize = 16) 
    ax5.set_xlabel('pH', fontsize = 16) 
    ax5.grid(True) 
    ax5.set_ylim(0, yc) 
    #ax5.set_xlim(0, 25) 
    ax5.legend(loc='upper right', fontsize = 10) 

    ax6.set_title("Organic content vs Th/K" , fontweight='bold', fontsize=25) 
    ax6.tick_params(axis='y', labelsize=12) 
    ax6.tick_params(axis='x', labelsize=12) 
    ax6.set_xlabel('Organic content [%]', fontsize = 16) 
    ax6.set_ylabel('Th / K ratio', fontsize = 16) 
    ax6.grid(True) 
    #ax6.set_xlim(0, 65) 
    ax6.set_ylim(0, yc)
    ax6.legend(loc='upper right', fontsize = 10) 


# Enhanced 3D plotting function with axis labels
def plot_3d(df, x, y, z, X, Y, Z, elev=30, azim=30):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df[x], df[y], df[z], c="navy", s=15)
    ax.plot_surface(X, Y, Z, alpha=0.5, color='orange', edgecolor='none')
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    plt.show()


def bars_plot(feature_sets, test_errors_summary, train_errors_summary, target_name):
    # Ensure the output folder exists, create it if it doesn't
    output_folder = 'figures_output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    fig, ax = plt.subplots()
    width = 0.35  # the width of the bars

    x = np.arange(len(feature_sets))
    rects1 = ax.bar(x - width/2, test_errors_summary, width, color = 'red', label='Test')
    rects2 = ax.bar(x + width/2, train_errors_summary, width, color = 'blue', label='Train')

    ax.axhline(0, color='grey', linewidth=0.8)
    ax.set_ylabel(target_name+' R2 scores')
    ax.set_xticks(range(len(test_errors_summary)), feature_sets, rotation = 15)
    ax.set_ylim(0, 1)
    ax.legend()
    fig.tight_layout()

    # Full file path
    full_file_path = os.path.join(output_folder, 'Bar_plot_'+target_name)

    # Save and show the figure
    plt.savefig(full_file_path, dpi=300, bbox_inches='tight')
    plt.show()


def fit_and_plot(df, x_cols, y_col, degree, mapping, ss=60, lw=0):
    x = df[x_cols]
    y = df[y_col]
    
    # Generate polynomial features
    poly = PolynomialFeatures(degree)
    x_poly = poly.fit_transform(x)
    
    # Fit a linear model
    model = LinearRegression()
    model.fit(x_poly, y)
    
    if len(x_cols) == 1:  # If there's only one predictor
        x_plot = np.linspace(x[x_cols[0]].min(), x[x_cols[0]].max(), 300).reshape(-1, 1)
        x_plot_poly = poly.transform(x_plot)
        y_plot = model.predict(x_plot_poly)
        y_plot = np.maximum(0, y_plot)  # Ensure y_plot is non-negative
        
        fig = go.Figure(data=[go.Scatter(x=x[x_cols[0]], y=y, mode='markers', name='Data points'),
                              go.Scatter(x=x_plot[:, 0], y=y_plot, mode='lines', name=f'Polynomial fit degree {degree}')])
        fig.update_layout(title='Polynomial Fit', xaxis_title=x_cols[0], yaxis_title=y_col, yaxis=dict(range=[0, max(y_plot)]))
        fig.show()
        
    elif len(x_cols) == 2:  # If there are two predictors
        # Generate grid for plots
        x0_range = np.linspace(x[x_cols[0]].min(), x[x_cols[0]].max(), 50)
        x1_range = np.linspace(x[x_cols[1]].min(), x[x_cols[1]].max(), 50)
        x0_grid, x1_grid = np.meshgrid(x0_range, x1_range)
        x_grid = np.c_[x0_grid.ravel(), x1_grid.ravel()]
        
        # Predict y values on grid
        x_grid_poly = poly.transform(x_grid)
        y_grid = model.predict(x_grid_poly).reshape(x0_grid.shape)
        y_grid = np.maximum(0, y_grid)  # Ensure y_grid is non-negative

        # Calculate R² score
        y_pred = model.predict(x_poly)
        r2 = r2_score(y, y_pred)
        
        # 3D surface plot
        fig = go.Figure(data=[go.Scatter3d(x=x[x_cols[0]], y=x[x_cols[1]], z=y, mode='markers', marker=dict(size=5), name='Data points'),
                              go.Surface(x=x0_range, y=x1_range, z=y_grid, name='Polynomial Surface')])
        fig.update_layout(title=f'3D Polynomial Fit (R² = {r2:.2f})', scene=dict(xaxis_title=x_cols[0], yaxis_title=x_cols[1], zaxis_title=y_col))
        fig.show()
        
        # 2D plots for each predictor
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        for i, col in enumerate(x_cols):
            x_plot = np.linspace(x[col].min(), x[col].max(), 300)
            x_plot_2d = np.column_stack([x_plot if i == j else np.full_like(x_plot, x[x_cols[j]].mean()) for j in range(2)])
            x_plot_poly = poly.transform(x_plot_2d)
            y_plot = model.predict(x_plot_poly)
            
            for start_str, (color, marker) in mapping.items():
                mask = df['SAMPLE'].str.startswith(start_str)
                filtered_df = df[mask]
                if not filtered_df.empty:  # Ensure there are points to plot and fit
                    axes[i].scatter(filtered_df[col], filtered_df[y_col], s=ss, linewidth=lw, c=color, marker=marker, label=f"{start_str} Site")

            axes[i].plot(x_plot, y_plot, color='red', label=f'Polynomial fit degree {degree}')
            axes[i].set_xlabel(col)
            axes[i].set_ylabel(y_col)
            axes[i].set_ylim(bottom=0)  # Ensure y-axis starts from 0
            axes[i].legend()
            axes[i].grid(True)
        
        plt.show()