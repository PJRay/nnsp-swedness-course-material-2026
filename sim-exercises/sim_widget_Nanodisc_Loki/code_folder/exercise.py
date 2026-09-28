from mcstasscript.jb_interface import SimInterface
import code_folder.Nanodisc_Loki_generated as nanodisc


class _WidgetParameterValues(dict):
    """Keep integral widget values valid for McStas integer parameters."""

    def __init__(self, instrument, values):
        self._integer_parameters = {
            parameter.name for parameter in instrument.parameters
            if parameter.type == "int"
        }
        super().__init__()
        for key, value in values.items():
            self[key] = value

    def __setitem__(self, key, value):
        if key in self._integer_parameters:
            try:
                numeric_value = float(value)
            except (TypeError, ValueError):
                pass
            else:
                if numeric_value.is_integer():
                    value = int(numeric_value)
        super().__setitem__(key, value)


def make():
    return nanodisc.make(input_path="code_folder")


def make_widget_interface():
    sim_interface = SimInterface(make())
    sim_interface.mpi = 4
    sim_interface.parameters = _WidgetParameterValues(
        sim_interface.instrument, sim_interface.parameters
    )
    return sim_interface


def show_widget():
    return make_widget_interface().show_interface()
