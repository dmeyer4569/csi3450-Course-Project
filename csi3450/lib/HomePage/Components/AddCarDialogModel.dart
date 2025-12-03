import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:image_picker/image_picker.dart';
import 'package:csi3450/HomePage/Components/getCarBloC/get_car_card_bloc.dart';

class AddCarDialog extends StatefulWidget {
  const AddCarDialog({super.key});

  // --- STATIC HELPER FOR POPUP ---
  static Future<void> show(BuildContext context) async {
    final bloc = BlocProvider.of<GetCarCardBloc>(context);

    await showDialog(
      context: context,
      builder: (dialogContext) {
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

  // Image Upload Variables
  File? _selectedImage;
  final ImagePicker _picker = ImagePicker();
  bool _showImageError = false; // To toggle red error text/border

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

  Future<void> _pickImage() async {
    final XFile? pickedFile = await _picker.pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        _selectedImage = File(pickedFile.path);
        _showImageError = false; // Clear error on successful pick
      });
    }
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
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // 1. Image Upload Section (REQUIRED)
                GestureDetector(
                  onTap: _pickImage,
                  child: Container(
                    height: 150,
                    decoration: BoxDecoration(
                      color: Colors.grey[200],
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(
                        color: _showImageError ? Colors.red : Colors.grey.shade400,
                        width: _showImageError ? 2.0 : 1.0,
                      ),
                      image: _selectedImage != null
                          ? DecorationImage(
                        image: FileImage(_selectedImage!),
                        fit: BoxFit.cover,
                      )
                          : null,
                    ),
                    child: _selectedImage == null
                        ? Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          Icons.add_a_photo,
                          size: 40,
                          color: _showImageError ? Colors.red : Colors.grey[600],
                        ),
                        const SizedBox(height: 8),
                        Text(
                          'Upload Image *',
                          style: TextStyle(
                            color: _showImageError ? Colors.red : Colors.grey[600],
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    )
                        : Stack(
                      children: [
                        Positioned(
                          right: 8,
                          top: 8,
                          child: Container(
                            padding: const EdgeInsets.all(4),
                            decoration: const BoxDecoration(
                              color: Colors.black54,
                              shape: BoxShape.circle,
                            ),
                            child: const Icon(Icons.edit, color: Colors.white, size: 20),
                          ),
                        )
                      ],
                    ),
                  ),
                ),
                if (_showImageError)
                  Padding(
                    padding: const EdgeInsets.only(top: 8.0, left: 4.0),
                    child: Text(
                      'Image is required',
                      style: TextStyle(color: Colors.red[700], fontSize: 12),
                    ),
                  ),

                const SizedBox(height: 15),

                // 2. Manufacturer Dropdown
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

                // 3. Model Input
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

                // 4. Year Input
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

                // 5. Base MSRP Input
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
            Navigator.of(context).pop();
          },
          child: const Text('Cancel', style: TextStyle(color: Colors.grey)),
        ),
        ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: Colors.black,
            foregroundColor: Colors.white,
          ),
          onPressed: () {
            // 1. Check Image Presence Manually (since it's not a FormField)
            if (_selectedImage == null) {
              setState(() {
                _showImageError = true;
              });
              // Stop execution if image is missing, even if form is valid
              return;
            }

            // 2. Validate Form Fields
            if (_formKey.currentState!.validate()) {
              final String newModel = _modelController.text;
              final int newYear = int.parse(_yearController.text);
              final int newMsrp = int.parse(_msrpController.text);
              final int manufacturerId = _selectedManufacturerId!;

              // 3. Trigger Bloc Event
              context.read<GetCarCardBloc>().add(
                LoadAddCar(
                  model: newModel,
                  year: newYear,
                  baseMsrp: newMsrp,
                  manufacturerId: manufacturerId,
                  imagePath: _selectedImage!.path,
                ),
              );

              if (kDebugMode) {
                print("Adding Car: $newModel, $newYear, $newMsrp, ManID: $manufacturerId, Img: ${_selectedImage!.path}");
              }

              Navigator.of(context).pop();
            }
          },
          child: const Text('Add Car'),
        ),
      ],
    );
  }
}