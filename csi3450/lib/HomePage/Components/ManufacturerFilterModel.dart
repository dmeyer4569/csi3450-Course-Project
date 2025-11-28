import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'getCarBloC/get_car_card_bloc.dart';

class ManufacturerFilterWidget extends StatefulWidget{
  final GetCarCardBloc carBloc;

  const ManufacturerFilterWidget({
    super.key,
    required this.carBloc
  });

  @override
  State<ManufacturerFilterWidget> createState() => _ManufacturerFilterWidgetState();
}

class _ManufacturerFilterWidgetState extends State<ManufacturerFilterWidget> {
  final scaffoldKey = GlobalKey<ScaffoldState>();

  int? _selectedManufacturerId;

  final Map<String, int> _manufacturerMap = {
    'None': 0,
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
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(10),
      child: Container(
        width: 210,
        padding: const EdgeInsets.symmetric(
          horizontal: 12,
          vertical: 4,
        ),
        decoration: BoxDecoration(
          border: Border.all(
            color: Colors.grey,
            width: 1,
          ),
          borderRadius: BorderRadius.circular(8),
        ),
        child: DropdownButtonHideUnderline(
          child: DropdownButton<int>(
            value: _selectedManufacturerId,

            isExpanded: true,
            hint: const Text("Select manufacturer..."),

            items: _manufacturerMap.entries.map((entry) {
              return DropdownMenuItem<int>(
                value: entry.value,
                child: Text(entry.key),
              );
            }).toList(),

            onChanged: (int? newValue) {
              if (newValue == null) return;

              setState(() {
                _selectedManufacturerId = newValue;
              });

              String selectedName = _manufacturerMap
                  .entries
                  .firstWhere(
                    (entry) => entry.value == newValue,
              )
                  .key;

              widget.carBloc.add(
                LoadCarsEvent(manufacturerId: newValue, manufacturerName: selectedName),
              );

            },
          ),
        ),
      ),
    );
  }
}