import 'package:csi3450/HomePage/Components/ManufacturerFilterModel.dart';
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
                          ManufacturerFilterWidget(carBloc: context.read<GetCarCardBloc>()),
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