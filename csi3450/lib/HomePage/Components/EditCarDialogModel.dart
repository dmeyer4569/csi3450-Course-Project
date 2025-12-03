import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:google_fonts/google_fonts.dart';

// Assuming you will create this event or it exists.
// If not, you can replace the bloc logic with a print statement for now.
import 'package:csi3450/HomePage/Components/getCarBloC/get_car_card_bloc.dart';

class EditCarDialog extends StatefulWidget {
  final int carId;
  final String currentModel;
  final int currentYear;
  final int currentBaseMsrp;
  final String currentManufacturerName;

  const EditCarDialog({
    super.key,
    required this.carId,
    required this.currentModel,
    required this.currentYear,
    required this.currentBaseMsrp,
    required this.currentManufacturerName,
  });

  // --- STATIC HELPER FOR POPUP ---
  // Call this method from your CarCardWidget to show the popup.
  // Usage: EditCarDialog.show(context, carId: ..., ...);
  static Future<void> show(
      BuildContext context, {
        required int carId,
        required String currentModel,
        required int currentYear,
        required int currentBaseMsrp,
        required String currentManufacturerName,
      }) async {
    // We capture the Bloc from the parent context so the Dialog can use it
    final bloc = BlocProvider.of<GetCarCardBloc>(context);

    await showDialog(
      context: context,
      builder: (dialogContext) {
        // We wrap the dialog in BlocProvider.value to ensure it can access the Bloc
        return BlocProvider.value(
          value: bloc,
          child: EditCarDialog(
            carId: carId,
            currentModel: currentModel,
            currentYear: currentYear,
            currentBaseMsrp: currentBaseMsrp,
            currentManufacturerName: currentManufacturerName,
          ),
        );
      },
    );
  }

  @override
  State<EditCarDialog> createState() => _EditCarDialogState();
}

class _EditCarDialogState extends State<EditCarDialog> {
  final _formKey = GlobalKey<FormState>();

  late TextEditingController _modelController;
  late TextEditingController _yearController;
  late TextEditingController _msrpController;
  late TextEditingController _manufacturerNameController; // New controller for display

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
    // --- PRE-FILL LOGIC ---
    _modelController = TextEditingController(text: widget.currentModel);
    _yearController = TextEditingController(text: widget.currentYear.toString());
    _msrpController = TextEditingController(text: widget.currentBaseMsrp.toString());

    // We use a controller just to display the name in the read-only field
    _manufacturerNameController = TextEditingController(text: widget.currentManufacturerName);

    // --- MAPPING LOGIC ---
    // We map the Name -> ID here so we have the Integer ready for the API call
    if (_manufacturerMap.containsKey(widget.currentManufacturerName)) {
      _selectedManufacturerId = _manufacturerMap[widget.currentManufacturerName];
    } else {
      // Handle edge case where name isn't in list (default to 0 or handled by backend)
      _selectedManufacturerId = 0;
    }
  }

  @override
  void dispose() {
    _modelController.dispose();
    _yearController.dispose();
    _msrpController.dispose();
    _manufacturerNameController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AlertDialog(
      title: Text(
        'Edit Car Details',
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
                // 1. Manufacturer Input (Read Only)
                // We show this first or last, but made it read-only as requested
                TextFormField(
                  controller: _manufacturerNameController,
                  enabled: false, // Disables interaction/editing
                  style: const TextStyle(color: Colors.grey), // Visual cue
                  decoration: const InputDecoration(
                    labelText: 'Manufacturer',
                    border: OutlineInputBorder(),
                    filled: true,
                    fillColor: Color(0xFFF0F0F0), // Light grey background
                  ),
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

              // Use the ID derived in initState
              final int manufacturerId = _selectedManufacturerId ?? 0;

              // 2. Dispatch Event to Bloc
              // NOTE: Replace this print with your actual Bloc event when ready
              context.read<GetCarCardBloc>().add(
                LoadEditCar(
                  carId: widget.carId,
                  model: newModel,
                  year: newYear,
                  baseMsrp: newMsrp,
                  manufacturerId: manufacturerId,
                ),
              );

              if (kDebugMode) {
                print("Updating Car ID: ${widget.carId}");
                print("New Data: $newModel, $newYear, $newMsrp, ManID: $manufacturerId");
              }

              Navigator.of(context).pop(); // Close dialog after saving
            }
          },
          child: const Text('Save Changes'),
        ),
      ],
    );
  }
}