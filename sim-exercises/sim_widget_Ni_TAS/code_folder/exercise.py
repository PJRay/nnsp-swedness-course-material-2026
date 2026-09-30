import copy

from mcstasscript.jb_interface import SimInterface
import code_folder.Ni_TAS_generated as ni_tas

from .scan import ParameterScan as Scan


def make():
    return ni_tas.make(input_path="code_folder")


def make_widget_interface():
    sim_interface = SimInterface(make())
    sim_interface.mpi = 4
    return sim_interface


def scan(sim_interface, parameter_name, start, stop, steps, monitor_name=None,
         **settings):
    """Scan a copy of the instrument configured by the widget."""
    scan_instrument = copy.deepcopy(sim_interface.instrument)
    scan_instrument.set_parameters(sim_interface.parameters)
    scan_settings = dict(settings)
    scan_settings.setdefault("mpi", sim_interface.mpi)
    scan_settings.setdefault("suppress_output", True)
    scan_settings.setdefault("output_path", "code_folder/scan_data")
    scan_instrument.settings(**scan_settings)
    return Scan(scan_instrument, parameter_name, start, stop, steps,
                monitor_name=monitor_name)
