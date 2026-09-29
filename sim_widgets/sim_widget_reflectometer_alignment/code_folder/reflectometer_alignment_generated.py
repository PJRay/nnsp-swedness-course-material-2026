#!/usr/bin/env python3
# Automatically generated file. 
# Format:    Python script code
# McStas <http://www.mcstas.org>
# Instrument: reflectometer_alignment.instr (reflectometer)
# Date:       Mon Sep 28 11:58:13 2026
# File:       reflectometer_alignment_generated.py

import mcstasscript as ms

# Python McStas instrument description
def make(input_path=None):
    instr = ms.McStas_instr("reflectometer_alignment_generated", author = "McCode Py-Generator", origin = "ESS DMSC", input_path=input_path)
    
# Add collected DEPENDENCY strings
    instr.set_dependency('')

    # *****************************************************************************
    # * Start of instrument 'reflectometer' generated code
    # *****************************************************************************
    # MCSTAS system dir is "/Users/user/miniforge3/envs/mcstasscript_mcstas/share/mcstas/resources/"


    # *****************************************************************************
    # * instrument 'reflectometer' and components DECLARE
    # *****************************************************************************

    # Instrument parameters:

    lambda_min = instr.add_parameter('double', 'lambda_min', value=5.3, comment='[AA] Minimum wavelength from source')
    lambda_max = instr.add_parameter('double', 'lambda_max', value=5.45, comment='[AA] Maximum wavelength from source')
    sampletranslation = instr.add_parameter('double', 'sampletranslation', value=0, comment='[m] Sample translation orthogonal to incoming beam')
    slitwidth = instr.add_parameter('double', 'slitwidth', value=0.0006, comment='[m] Width of slit pinholes')
    slitheight = instr.add_parameter('double', 'slitheight', value=0.08, comment='[m] Height of slit pinholes')
    dist_slit2slit = instr.add_parameter('double', 'dist_slit2slit', value=3.2, comment='[m] Distance between slits')
    dist_sample2detector = instr.add_parameter('double', 'dist_sample2detector', value=2, comment='[m] Distance between sample and detector')
    sampletype = instr.add_parameter('double', 'sampletype', value=1, options=[0,1], comment='[1] Sample type: 0 none, 1 mirror, 2+ multilayer')
    MR_Qc = instr.add_parameter('double', 'MR_Qc', value=0.017, comment='[AA^-1] Critical Q-vector length of mirror sample')
    sampleangle = instr.add_parameter('double', 'sampleangle', value=0.2, comment='[deg] Rotation angle of sample aka theta')
    detectorangle = instr.add_parameter('double', 'detectorangle', value=0, comment='[deg] Rotation angle of detector window aka 2 theta')
    beamstop = instr.add_parameter('double', 'beamstop', value=0, options=[0,1], comment='[1] If 0 the beamstop is out, if 1 it is in')

    component_definition_metadata = {
    }
    instr.append_declare(r'''
double blocktranslation;
double slittranslation      = 0;
double dist_source2slit     = 1;
double dist_slit2sample     = 0.08;//Distance between second slit and sample center
double samplesize           = 0.15;
double substratethickness   = 0.003;// Thickness of the incoherently and absorbing part of the sample

    ''')


    instr.append_initialize(r'''
  blocktranslation = -slittranslation;//If set translates everything after the second sample slit

    ''')


    # *****************************************************************************
    # * instrument 'reflectometer' TRACE
    # *****************************************************************************
    
    # Comp instance Origin, placement and parameters
    Origin = instr.add_component('Origin','Progress_bar')
    
    Origin.profile = '"NULL"'
    Origin.percent = '10'
    Origin.flag_save = '0'
    Origin.minutes = '0'
    
    # Comp instance Source, placement and parameters
    Source = instr.add_component('Source','Source_Maxwell_3', AT=['0', '0', '0'], AT_RELATIVE='Origin', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Origin')
    
    Source.size = '0'
    Source.yheight = '0.12'
    Source.xwidth = '0.12'
    Source.Lmin = 'lambda_min'
    Source.Lmax = 'lambda_max'
    Source.dist = 'dist_source2slit + dist_slit2slit'
    Source.focus_xw = 'slitwidth'
    Source.focus_yh = 'slitheight'
    Source.T1 = '150.42'
    Source.T2 = '38.72'
    Source.T3 = '14.84'
    Source.I1 = '3.67E11'
    Source.I2 = '3.64E11'
    Source.I3 = '0.95E11'
    Source.target_index = '1'
    Source.lambda0 = '0'
    Source.dlambda = '0'
    
    # Comp instance Slit1, placement and parameters
    Slit1 = instr.add_component('Slit1','Slit', AT=['0', '0', 'dist_source2slit'], AT_RELATIVE='Source', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Source')
    
    Slit1.xmin = 'UNSET'
    Slit1.xmax = 'UNSET'
    Slit1.ymin = 'UNSET'
    Slit1.ymax = 'UNSET'
    Slit1.radius = 'UNSET'
    Slit1.xwidth = 'slitwidth'
    Slit1.yheight = 'slitheight'
    
    # Comp instance Slit2, placement and parameters
    Slit2 = instr.add_component('Slit2','Slit', AT=['0', '0', 'dist_slit2slit'], AT_RELATIVE='Slit1', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Slit1')
    
    Slit2.xmin = 'UNSET'
    Slit2.xmax = 'UNSET'
    Slit2.ymin = 'UNSET'
    Slit2.ymax = 'UNSET'
    Slit2.radius = 'UNSET'
    Slit2.xwidth = 'slitwidth'
    Slit2.yheight = 'slitheight'
    
    # Comp instance Arm_sampleNOROTNOTRANS, placement and parameters
    Arm_sampleNOROTNOTRANS = instr.add_component('Arm_sampleNOROTNOTRANS','Arm', AT=['blocktranslation', '0', 'dist_slit2sample'], AT_RELATIVE='Slit2', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Slit2')
    
    
    # Comp instance Arm_sampleNOROT, placement and parameters
    Arm_sampleNOROT = instr.add_component('Arm_sampleNOROT','Arm', AT=['sampletranslation', '0', '0'], AT_RELATIVE='Arm_sampleNOROTNOTRANS', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Arm_sampleNOROTNOTRANS')
    
    
    # Comp instance Arm_sample, placement and parameters
    Arm_sample = instr.add_component('Arm_sample','Arm', AT=['0', '0', '0'], AT_RELATIVE='Arm_sampleNOROT', ROTATED=['0', 'sampleangle', '0'], ROTATED_RELATIVE='Arm_sampleNOROT')
    
    
    # Comp instance Mirror_1_position, placement and parameters
    Mirror_1_position = instr.add_component('Mirror_1_position','Arm', AT=['0', '0', '0'], AT_RELATIVE='Arm_sample', ROTATED=['0', '90', '0'], ROTATED_RELATIVE='Arm_sample')
    
    
    # Comp instance Sample_Mirror_backside_before, placement and parameters
    Sample_Mirror_backside_before = instr.add_component('Sample_Mirror_backside_before','Isotropic_Sqw', AT=['0', '0', '- substratethickness / 2 -1e-6'], AT_RELATIVE='Mirror_1_position', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Mirror_1_position')
    # WHEN ( sampletype == 1 && sampleangle < 0 ) at Sample_Mirror_backside_before
    Sample_Mirror_backside_before.set_WHEN('( sampletype == 1 && sampleangle < 0 )')
    
    Sample_Mirror_backside_before.powder_format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
    Sample_Mirror_backside_before.Sqw_coh = '0'
    Sample_Mirror_backside_before.Sqw_inc = '0'
    Sample_Mirror_backside_before.geometry = '0'
    Sample_Mirror_backside_before.radius = '0'
    Sample_Mirror_backside_before.thickness = '0'
    Sample_Mirror_backside_before.xwidth = 'samplesize'
    Sample_Mirror_backside_before.yheight = 'samplesize'
    Sample_Mirror_backside_before.zdepth = 'substratethickness'
    Sample_Mirror_backside_before.threshold = '1e-20'
    Sample_Mirror_backside_before.order = '0'
    Sample_Mirror_backside_before.T = '0'
    Sample_Mirror_backside_before.verbose = '1'
    Sample_Mirror_backside_before.d_phi = '0'
    Sample_Mirror_backside_before.concentric = '0'
    Sample_Mirror_backside_before.rho = '0.1'
    Sample_Mirror_backside_before.sigma_abs = '1'
    Sample_Mirror_backside_before.sigma_coh = '0'
    Sample_Mirror_backside_before.sigma_inc = '1'
    Sample_Mirror_backside_before.classical = '-1'
    Sample_Mirror_backside_before.powder_Dd = '0'
    Sample_Mirror_backside_before.powder_DW = '0'
    Sample_Mirror_backside_before.powder_Vc = '0'
    Sample_Mirror_backside_before.density = '0'
    Sample_Mirror_backside_before.weight = '0'
    Sample_Mirror_backside_before.p_interact = '-1'
    Sample_Mirror_backside_before.norm = '-1'
    Sample_Mirror_backside_before.powder_barns = '1'
    Sample_Mirror_backside_before.quantum_correction = '"Frommhold"'
    
    # Comp instance Sample_Mirror, placement and parameters
    Sample_Mirror = instr.add_component('Sample_Mirror','Mirror', AT=['0', '0', '0'], AT_RELATIVE='Arm_sample', ROTATED=['0', '90', '0'], ROTATED_RELATIVE='Arm_sample')
    # WHEN ( sampletype == 1 ) at Sample_Mirror
    Sample_Mirror.set_WHEN('( sampletype == 1 )')
    
    Sample_Mirror.reflect = '0'
    Sample_Mirror.xwidth = 'samplesize'
    Sample_Mirror.yheight = 'samplesize'
    Sample_Mirror.R0 = '0.99'
    Sample_Mirror.Qc = 'MR_Qc'
    Sample_Mirror.alpha = '6.07'
    Sample_Mirror.m = '1'
    Sample_Mirror.W = '0.003'
    Sample_Mirror.center = '1'
    Sample_Mirror.transmit = '1'
    
    # Comp instance Sample_Mirror_backside_after, placement and parameters
    Sample_Mirror_backside_after = instr.add_component('Sample_Mirror_backside_after','Isotropic_Sqw', AT=['0', '0', '- substratethickness / 2 -1e-6'], AT_RELATIVE='Sample_Mirror', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Sample_Mirror')
    # WHEN ( sampletype == 1 && sampleangle >= 0 ) at Sample_Mirror_backside_after
    Sample_Mirror_backside_after.set_WHEN('( sampletype == 1 && sampleangle >= 0 )')
    
    Sample_Mirror_backside_after.powder_format = '{ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 }'
    Sample_Mirror_backside_after.Sqw_coh = '0'
    Sample_Mirror_backside_after.Sqw_inc = '0'
    Sample_Mirror_backside_after.geometry = '0'
    Sample_Mirror_backside_after.radius = '0'
    Sample_Mirror_backside_after.thickness = '0'
    Sample_Mirror_backside_after.xwidth = 'samplesize'
    Sample_Mirror_backside_after.yheight = 'samplesize'
    Sample_Mirror_backside_after.zdepth = 'substratethickness'
    Sample_Mirror_backside_after.threshold = '1e-20'
    Sample_Mirror_backside_after.order = '0'
    Sample_Mirror_backside_after.T = '0'
    Sample_Mirror_backside_after.verbose = '1'
    Sample_Mirror_backside_after.d_phi = '0'
    Sample_Mirror_backside_after.concentric = '0'
    Sample_Mirror_backside_after.rho = '0.1'
    Sample_Mirror_backside_after.sigma_abs = '1'
    Sample_Mirror_backside_after.sigma_coh = '0'
    Sample_Mirror_backside_after.sigma_inc = '1'
    Sample_Mirror_backside_after.classical = '-1'
    Sample_Mirror_backside_after.powder_Dd = '0'
    Sample_Mirror_backside_after.powder_DW = '0'
    Sample_Mirror_backside_after.powder_Vc = '0'
    Sample_Mirror_backside_after.density = '0'
    Sample_Mirror_backside_after.weight = '0'
    Sample_Mirror_backside_after.p_interact = '-1'
    Sample_Mirror_backside_after.norm = '-1'
    Sample_Mirror_backside_after.powder_barns = '1'
    Sample_Mirror_backside_after.quantum_correction = '"Frommhold"'
    
    # Comp instance Arm_detectorONLYROT, placement and parameters
    Arm_detectorONLYROT = instr.add_component('Arm_detectorONLYROT','Arm', AT=['0', '0', '0'], AT_RELATIVE='Arm_sampleNOROTNOTRANS', ROTATED=['0', 'detectorangle', '0'], ROTATED_RELATIVE='Source')
    
    
    # Comp instance Arm_detector, placement and parameters
    Arm_detector = instr.add_component('Arm_detector','Arm', AT=['0', '0', 'dist_sample2detector'], AT_RELATIVE='Arm_detectorONLYROT', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Arm_detectorONLYROT')
    
    
    # Comp instance beamstop, placement and parameters
    beamstop = instr.add_component('beamstop','Beamstop', AT=['0', '0', 'dist_sample2detector -0.02'], AT_RELATIVE='Arm_sampleNOROTNOTRANS', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Arm_sampleNOROTNOTRANS')
    # WHEN ( beamstop ) at beamstop
    beamstop.set_WHEN('( beamstop )')
    
    beamstop.xmin = '-0.05'
    beamstop.xmax = '0.05'
    beamstop.ymin = '-0.05'
    beamstop.ymax = '0.05'
    beamstop.xwidth = '0.003'
    beamstop.yheight = '0.20'
    beamstop.radius = '0'
    
    # Comp instance DetectorWindow, placement and parameters
    DetectorWindow = instr.add_component('DetectorWindow','PSD_monitor', AT=['0', '0', '0'], AT_RELATIVE='Arm_detector', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Arm_detector')
    
    DetectorWindow.nx = '4'
    DetectorWindow.ny = '50'
    DetectorWindow.filename = '"mon_detector_window"'
    DetectorWindow.xmin = '-0.05'
    DetectorWindow.xmax = '0.05'
    DetectorWindow.ymin = '-0.05'
    DetectorWindow.ymax = '0.05'
    DetectorWindow.xwidth = '0.008'
    DetectorWindow.yheight = '0.2'
    DetectorWindow.restore_neutron = '1'
    DetectorWindow.nowritefile = '0'
    
    # Comp instance Detector, placement and parameters
    Detector = instr.add_component('Detector','PSD_monitor', AT=['0', '0', 'dist_sample2detector + 0.001'], AT_RELATIVE='Arm_sampleNOROTNOTRANS', ROTATED=['0.0', '0.0', '0.0'], ROTATED_RELATIVE='Arm_sampleNOROTNOTRANS')
    
    Detector.nx = '100'
    Detector.ny = '50'
    Detector.filename = '"mon_detector"'
    Detector.xmin = '-0.05'
    Detector.xmax = '0.05'
    Detector.ymin = '-0.05'
    Detector.ymax = '0.05'
    Detector.xwidth = '0.2'
    Detector.yheight = '0.2'
    Detector.restore_neutron = '1'
    Detector.nowritefile = '0'
    
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


# end of generated Python code reflectometer_alignment_generated.py 
