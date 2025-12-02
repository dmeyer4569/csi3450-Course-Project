import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'getCarBloC/get_car_card_bloc.dart';

class MSRPFilterWidget extends StatefulWidget{
  final GetCarCardBloc carBloc;

  const MSRPFilterWidget({
    super.key,
    required this.carBloc
  });

  @override
  State<MSRPFilterWidget> createState() => _MSRPFilterWidgetState();
}

class _MSRPFilterWidgetState extends State<MSRPFilterWidget> {
  final scaffoldKey = GlobalKey<ScaffoldState>();

  int? _selectedManufacturerId;

  final Map<String, int> _manufacturerMap = {
    'None': 4,
    'Descending': 2,
    'Ascending': 3,
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
            hint: const Text("Filter MSRP..."),

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