import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:csi3450/HomePage/Components/getCarBloC/get_car_card_bloc.dart';

class AddCarDialog extends StatefulWidget {
  const AddCarDialog({super.key});

  // --- STATIC HELPER FOR POPUP ---
  // Call this method from your AddCarCardWidget to show the popup.
  // Usage: AddCarDialog.show(context);
  static Future<void> show(BuildContext context) async {
    // We capture the Bloc from the parent context so the Dialog can use it
    final bloc = BlocProvider.of<GetCarCardBloc>(context);

    await showDialog(
      context: context,
      builder: (dialogContext) {
        // We wrap the dialog in BlocProvider.value to ensure it can access the Bloc
        return BlocProvider.value(
          value: bloc,
          child: const AddCarDialog(),
        );
      },
    );
  }

  @override
  State<AddCarDialog> createState() => _AddCarDialogState();
}

class _AddCarDialogState extends State<AddCarDialog> {
  final _formKey = GlobalKey<FormState>();

  late TextEditingController _modelController;
  late TextEditingController _yearController;
  late TextEditingController _msrpController;

  int? _selectedManufacturerId;

  // Exact map from your reference
  final Map<String, int> _manufacturerMap = {
    'Ford': 1,
    'Toyota': 2,
    'Honda': 3,
    'BMW': 4,
    'Tesla': 5,
    'Mercedes': 6,
    'Audi': 7,
    'Ferrari': 8,
    'Lamborghini': 9,
    'Volkswagen': 10,
    'McLaren': 11,
    'Pagani': 12,
    'Koenigsegg': 13,
    'Renault': 14,
    'Bugatti': 15
  };

  @override
  void initState() {
    super.initState();
    // Initialize empty controllers for new data
    _modelController = TextEditingController();
    _yearController = TextEditingController();
    _msrpController = TextEditingController();
  }

  @override
  void dispose() {
    _modelController.dispose();
    _yearController.dispose();
    _msrpController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text(
        'Add New Car',
        style: GoogleFonts.inter(fontWeight: FontWeight.bold),
      ),
      content: SingleChildScrollView(
        child: Container(
          width: double.maxFinite,
          child: Form(
            key: _formKey,
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                // 1. Manufacturer Dropdown (Functional)
                DropdownButtonFormField<int>(
                  value: _selectedManufacturerId,
                  decoration: const InputDecoration(
                    labelText: 'Manufacturer',
                    border: OutlineInputBorder(),
                    filled: true,
                    fillColor: Colors.white,
                  ),
                  items: _manufacturerMap.entries.map((entry) {
                    return DropdownMenuItem<int>(
                      value: entry.value,
                      child: Text(entry.key),
                    );
                  }).toList(),
                  onChanged: (value) {
                    setState(() {
                      _selectedManufacturerId = value;
                    });
                  },
                  validator: (value) {
                    if (value == null || value == 0) {
                      return 'Please select a manufacturer';
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 15),

                // 2. Model Input
                TextFormField(
                  controller: _modelController,
                  decoration: const InputDecoration(
                    labelText: 'Model',
                    border: OutlineInputBorder(),
                  ),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter a model';
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 15),

                // 3. Year Input
                TextFormField(
                  controller: _yearController,
                  decoration: const InputDecoration(
                    labelText: 'Year',
                    border: OutlineInputBorder(),
                  ),
                  keyboardType: TextInputType.number,
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter a year';
                    }
                    if (int.tryParse(value) == null) {
                      return 'Enter a valid number';
                    }
                    return null;
                  },
                ),
                const SizedBox(height: 15),

                // 4. Base MSRP Input
                TextFormField(
                  controller: _msrpController,
                  decoration: const InputDecoration(
                    labelText: 'Base MSRP',
                    prefixText: '\$ ',
                    border: OutlineInputBorder(),
                  ),
                  keyboardType: TextInputType.number,
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'Please enter MSRP';
                    }
                    if (int.tryParse(value) == null) {
                      return 'Enter a valid number';
                    }
                    return null;
                  },
                ),
              ],
            ),
          ),
        ),
      ),
      actions: [
        TextButton(
          onPressed: () {
            Navigator.of(context).pop(); // Close dialog
          },
          child: const Text('Cancel', style: TextStyle(color: Colors.grey)),
        ),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.black,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            if (_formKey.currentState!.validate()) {
              // 1. Extract values
              final String newModel = _modelController.text;
              final int newYear = int.parse(_yearController.text);
              final int newMsrp = int.parse(_msrpController.text);
              final int manufacturerId = _selectedManufacturerId!;

              // 2. Dispatch Event to Bloc
              // Ensure 'LoadAddCar' exists in your Bloc events
              context.read<GetCarCardBloc>().add(
                LoadAddCar(
                  model: newModel,
                  year: newYear,
                  baseMsrp: newMsrp,
                  manufacturerId: manufacturerId,
                ),
              );

              if (kDebugMode) {
                print("Adding New Car: $newModel, $newYear, $newMsrp, ManID: $manufacturerId");
              }

              Navigator.of(context).pop(); // Close dialog after saving
            }
          },
          child: const Text('Add Car'),
        ),
      ],
    );
  }
}