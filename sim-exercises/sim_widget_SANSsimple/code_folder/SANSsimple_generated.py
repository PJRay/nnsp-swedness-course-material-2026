#!/usr/bin/env python3
# Automatically generated file. 
# Format:    Python script code
# McStas <http://www.mcstas.org>
# Instrument: SANSsimple.instr (SANS2_liposomes)
# Date:       Mon Sep 28 11:56:09 2026
# File:       /Users/user/Projects/Teaching/summer_school/NNSP_2026/nnsp-sweness-course-material-2026/sim-exercises/SANSsimple/code_folder/SANSsimple_generated.py

import mcstasscript as ms

# Python McStas instrument description
def make(input_path=None):
    instr = ms.McStas_instr("SANS2_liposomes_generated", author = "McCode Py-Generator", origin = "ESS DMSC", input_path=input_path)
    
# Add collected DEPENDENCY strings
    instr.set_dependency('')

    # *****************************************************************************
    # * Start of instrument 'SANS2_liposomes' generated code
    # *****************************************************************************
    # MCSTAS system dir is "/Users/user/miniforge3/envs/mcstasscript_mcstas/share/mcstas/resources/"


    # *****************************************************************************
    # * instrument 'SANS2_liposomes' and components DECLARE
    # *****************************************************************************

    # Instrument parameters:

    pinhole_rad = instr.add_parameter('double', 'pinhole_rad', value=0.004, comment='[m] radius of the collimating pinholes')
    LC = instr.add_parameter('double', 'LC', value=3, comment='[m] length of the collimator - distance between pinholes')
    LD = instr.add_parameter('double', 'LD', value=3, comment='[m] distance between the last pinhole slit and detector')
    Lambda = instr.add_parameter('double', 'Lambda', value=6, comment='[AA] Average wavelength traced from source')
    DLambda = instr.add_parameter('double', 'DLambda', value=0.6, comment='[AA] Wavelength band +/- traced from source')
    R = instr.add_parameter('double', 'R', value=400, comment='[AA] radius of the hard, monodisperse spheres in the sample')
    dR = instr.add_parameter('double', 'dR', value=0, comment='[AA] Normal variance of Radius')
    dbilayer = instr.add_parameter('double', 'dbilayer', value=35, comment='[AA] Thickness of spherical shell, only relevant when SAMPLE==2')
    PHI = instr.add_parameter('double', 'PHI', value=1e-2, comment='[1] Volumefraction of the hard, monodisperse spheres in the sample')
    Delta_Rho = instr.add_parameter('double', 'Delta_Rho', value=0.6, comment='[fm/AA^3] Volume specific scattering length density contrast of the hard, monodisperse spheres in the sample as compared to the solution')
    Qmax = instr.add_parameter('double', 'Qmax', value=0.3, comment='[AA^-1] Maximum scattering vector allowed by geometry to hit the detector area')
    BEAMSTOP = instr.add_parameter('double', 'BEAMSTOP', value=1, options=[0,1], comment='[0/1] If set, the beamstop is inserted in front of the detector in order to block the transmitted beam')
    SAMPLE = instr.add_parameter('double', 'SAMPLE', value=1, options=[0,1,2], comment='[0/1/2] When SAMPLE==0, no sample is used, SAMPLE==1 sample is composed of hard spheres, if SAMPLE==2 sample is composed of spherical shells.')
    Sigma_a = instr.add_parameter('double', 'Sigma_a', value=0, comment='[barn] Absorption crossection of the sample')

    component_definition_metadata = {
    }
    instr.append_declare(r'''
double nm=1e-9;
double Rdet;
    ''')


    instr.append_initialize(r'''
  Rdet=0.5; // Radius of detector, also used for focusing sample
    ''')


    # *****************************************************************************
    # * instrument 'SANS2_liposomes' TRACE
    # *****************************************************************************
    
    # Comp instance Origin, placement and parameters
    Origin = instr.add_component('Origin','Progress_bar')
    
    Origin.profile = '"NULL"'
    Origin.percent = '10'
    Origin.flag_save = '0'
    Origin.minutes = '0'
    
    # Comp instance source, placement and parameters
    source = instr.add_component('source','Source_Maxwell_3', AT=['0', '0', '0'], AT_RELATIVE='Origin', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Origin')
    
    source.size = '2 * pinhole_rad'
    source.yheight = '0'
    source.xwidth = '0'
    source.Lmin = 'Lambda - DLambda'
    source.Lmax = 'Lambda + DLambda'
    source.dist = 'LC'
    source.focus_xw = 'pinhole_rad'
    source.focus_yh = 'pinhole_rad'
    source.T1 = '150.42'
    source.T2 = '38.74'
    source.T3 = '14.84'
    source.I1 = '3.67e11'
    source.I2 = '3.64e11'
    source.I3 = '0.95e11'
    source.target_index = '1'
    source.lambda0 = '0'
    source.dlambda = '0'
    
    # Comp instance ArmSlit1, placement and parameters
    ArmSlit1 = instr.add_component('ArmSlit1','Arm', AT=['0', '0', '6 - LC + 0.001'], AT_RELATIVE='source', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='source')
    
    
    # Comp instance CircSlit1, placement and parameters
    CircSlit1 = instr.add_component('CircSlit1','Slit', AT=['0', '0', '0'], AT_RELATIVE='ArmSlit1', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='ArmSlit1')
    
    CircSlit1.xmin = 'UNSET'
    CircSlit1.xmax = 'UNSET'
    CircSlit1.ymin = 'UNSET'
    CircSlit1.ymax = 'UNSET'
    CircSlit1.radius = 'pinhole_rad'
    CircSlit1.xwidth = 'UNSET'
    CircSlit1.yheight = 'UNSET'
    
    # Comp instance ArmSlit2, placement and parameters
    ArmSlit2 = instr.add_component('ArmSlit2','Arm', AT=['0', '0', '6'], AT_RELATIVE='source', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='source')
    
    
    # Comp instance CircSlit2, placement and parameters
    CircSlit2 = instr.add_component('CircSlit2','Slit', AT=['0', '0', '0'], AT_RELATIVE='ArmSlit2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='ArmSlit2')
    
    CircSlit2.xmin = 'UNSET'
    CircSlit2.xmax = 'UNSET'
    CircSlit2.ymin = 'UNSET'
    CircSlit2.ymax = 'UNSET'
    CircSlit2.radius = 'pinhole_rad'
    CircSlit2.xwidth = 'UNSET'
    CircSlit2.yheight = 'UNSET'
    
    # Comp instance SampleArm, placement and parameters
    SampleArm = instr.add_component('SampleArm','Arm', AT=['0', '0', '0.05'], AT_RELATIVE='ArmSlit2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='ArmSlit2')
    
    
    # Comp instance sampleB, placement and parameters
    sampleB = instr.add_component('sampleB','Sans_liposomes_new', AT=['0', '0', '0'], AT_RELATIVE='SampleArm', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='SampleArm')
    # SPLIT 10 times at sampleB
    sampleB.set_SPLIT('10')
    # WHEN ( SAMPLE == 1 ) at sampleB
    sampleB.set_WHEN('( SAMPLE == 1 )')
    
    sampleB.R = 'R'
    sampleB.dR = 'dR'
    sampleB.Phi = 'PHI'
    sampleB.Delta_rho = 'Delta_Rho'
    sampleB.sigma_a = '0.5'
    sampleB.dist = 'LD'
    sampleB.Rdet = 'Rdet'
    sampleB.xwidth = '4 * pinhole_rad'
    sampleB.yheight = '4 * pinhole_rad'
    sampleB.zthick = '0.005'
    sampleB.qmax = 'Qmax'
    sampleB.dbilayer = '35'
    
    # Comp instance beamstop, placement and parameters
    beamstop = instr.add_component('beamstop','Beamstop', AT=['0', '0', 'LD -0.01'], AT_RELATIVE='ArmSlit2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='ArmSlit2')
    # WHEN ( BEAMSTOP ) at beamstop
    beamstop.set_WHEN('( BEAMSTOP )')
    
    beamstop.xmin = '-0.05'
    beamstop.xmax = '0.05'
    beamstop.ymin = '-0.05'
    beamstop.ymax = '0.05'
    beamstop.xwidth = '0'
    beamstop.yheight = '0'
    beamstop.radius = '3 * pinhole_rad'
    
    # Comp instance PSD, placement and parameters
    PSD = instr.add_component('PSD','PSD_monitor', AT=['0', '0', 'LD -0.001'], AT_RELATIVE='ArmSlit2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='ArmSlit2')
    
    PSD.nx = '128'
    PSD.ny = '128'
    PSD.filename = '"PSD.txt"'
    PSD.xmin = '-0.05'
    PSD.xmax = '0.05'
    PSD.ymin = '-0.05'
    PSD.ymax = '0.05'
    PSD.xwidth = '1'
    PSD.yheight = '1'
    PSD.restore_neutron = '1'
    PSD.nowritefile = '0'
    
    # Comp instance q_monitor, placement and parameters
    q_monitor = instr.add_component('q_monitor','SANSQMonitor', AT=['0', '0', 'LD + 0.001'], AT_RELATIVE='ArmSlit2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='ArmSlit2')
    
    q_monitor.NumberOfBins = '100'
    q_monitor.RFilename = '"rdetector"'
    q_monitor.qFilename = '"qdetector"'
    q_monitor.RadiusDetector = 'Rdet'
    q_monitor.DistanceFromSample = 'LD'
    q_monitor.LambdaMin = 'Lambda - DLambda'
    q_monitor.Lambda0 = '0.0'
    q_monitor.restore_neutron = '1'
    
    # Instruct McStasscript not to 'check everythng'
    instr.settings(checks=False)
    return instr


if __name__ == '__main__':
    instr=make()
    # Use instr.settings() to add e.g. seed=1000, ncount=1e7, mpi=8, openacc=True, force_compile=False etc.)
    

# Show diagram
    instr.show_diagram()
    

# Visualise with default parameters (defaults to 'webgl-legacy' visualisation)
    instr.show_instrument()
    

# Generate a dataset with default parameters.
    data = instr.backengine()
    
# Overview plot:
    ms.make_sub_plot(data)
    

# Other useful commands follow...
    
# One plot pr. window
    #ms.make_plot(data)
    
# Load another dataset
    #data2 = ms.load_data('some_other_folder')
    
# Adjusting a specific plot
    #ms.name_plot_options("PSD_4PI", data, log=1, colormap="hot", orders_of_mag=5)
    

# Bring up the 'interface' - only relevant in Jupyter
    #%matplotlib widget
    #import mcstasscript.jb_interface as ms_widget
    #ms_widget.show(data)
    

# Bring up the simulation 'interface' - only relevant in Jupyter
    #%matplotlib widget
    #import mcstasscript.jb_interface as ms_widget
    #sim_widget = ms_widget.SimInterface(instr)
    #sim_widget.show_interface()
    

# Acessing data from the interface
    #data = sim_widget.get_data()


# end of generated Python code /Users/user/Projects/Teaching/summer_school/NNSP_2026/nnsp-sweness-course-material-2026/sim-exercises/SANSsimple/code_folder/SANSsimple_generated.py 
