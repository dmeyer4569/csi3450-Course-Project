import 'package:flutter_bloc/flutter_bloc.dart';

import './Components/CarCardModel.dart';
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import 'Components/getCarBloC/get_car_card_bloc.dart';
import 'HomePageModel.dart';
export 'HomePageModel.dart';

class HomePageWidget extends StatefulWidget {
  const HomePageWidget({super.key});

  static String routeName = 'HomePage';
  static String routePath = '/homePage';

  @override
  State<HomePageWidget> createState() => _HomePageWidgetState();
}

class _HomePageWidgetState extends State<HomePageWidget> {
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
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        FocusScope.of(context).unfocus();
        FocusManager.instance.primaryFocus?.unfocus();
      },
      child: Scaffold(
        key: scaffoldKey,
        backgroundColor: Colors.white,
        appBar: AppBar(
          backgroundColor: Colors.purple,
          automaticallyImplyLeading: false,
          title: Text(
            'Car Website',
            style: GoogleFonts.interTight(
              fontWeight: FontWeight.w500,
              color: Colors.white,
              fontSize: 22,
            ),
          ),
          centerTitle: false,
          elevation: 2,
        ),
        body: SafeArea(
          top: true,
          child: BlocProvider(
            create: (context) =>
                GetCarCardBloc()..add(LoadCarsEvent(manufacturerId: 0, manufacturerName: "empty")),
            child: Builder(
              builder: (context) {
                return BlocBuilder<GetCarCardBloc, GetCarCardState>(
                  builder: (context, state) {
                    if (state is GetCarCardInitialState) {
                      return Container();
                    } else if (state is GetCarCardLoadingState) {
                      return Center(child: CircularProgressIndicator());
                    } else if (state is GetCarCardLoadedState) {
                      List<CarCardWidget> uiCarCard = state.carCardModel;
                      return Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Padding(
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

                                    context.read<GetCarCardBloc>().add(
                                      LoadCarsEvent(manufacturerId: newValue, manufacturerName: selectedName),
                                    );

                                  },
                                ),
                              ),
                            ),
                          ),
                          Expanded(
                            child: GridView.builder(
                              itemCount: uiCarCard.length,
                              padding: const EdgeInsets.all(20),

                              gridDelegate:
                                  const SliverGridDelegateWithMaxCrossAxisExtent(
                                    maxCrossAxisExtent: 220,
                                    mainAxisExtent: 280,
                                    crossAxisSpacing: 20,
                                    mainAxisSpacing: 20,
                                  ),

                              itemBuilder: (BuildContext context, int index) {
                                return uiCarCard[index];
                              },
                            ),
                          ),
                        ],
                      );
                    }
                    return Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const Text("Complete Failure! :D"),
                          const SizedBox(height: 20),
                          ElevatedButton.icon(
                            icon: const Icon(Icons.refresh),
                            label: const Text("Refresh"),
                            onPressed: () {
                              context.read<GetCarCardBloc>().add(
                                LoadCarsEvent(manufacturerId: 0, manufacturerName: "empty"),
                              );
                            },
                          ),
                        ],
                      ),
                    );
                  },
                );
              },
            ),
          ),
        ),
      ),
    );
  }
}
