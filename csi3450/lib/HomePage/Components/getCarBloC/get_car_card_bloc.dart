import 'package:bloc/bloc.dart';
import 'package:csi3450/HomePage/Components/ResponseModels/Returns/GetManufacturerCarsResponse.dart';
import 'package:equatable/equatable.dart';
import 'package:flutter/foundation.dart';

import '../CarCardModel.dart';
import '../ResponseModels/Returns/GetCarsResponse.dart';
import '../ResponseModels/api.dart';

part 'get_car_card_event.dart';
part 'get_car_card_state.dart';

class GetCarCardBloc extends Bloc<GetCarCardEvent, GetCarCardState> {
  GetCarCardBloc() : super(GetCarCardInitialState()) {
    late int valueManufacturerId;
    late String manufacturerName;

    on<LoadCarsEvent>((event, emit) async {
      emit(GetCarCardLoadingState());

      try {
        valueManufacturerId = event.manufacturerId;
        late final List<CarCardWidget> uiCars;

        if (valueManufacturerId == 0) {
          final List<GetCarsResponse>? getCarsResponse = await Api.getCars();

          if (getCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: car.manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carPath,
            );
          }).toList();
        } else {
          final List<GetManufacturersCarResponse>? getManufacturersCarsResponse = await Api.getManufacturerCars(valueManufacturerId);

          if (getManufacturersCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          manufacturerName = event.manufacturerName;

          uiCars = getManufacturersCarsResponse.map((car) {
            return CarCardWidget(
                carId: car.carId,
                model: car.model ?? "Unknown Model",
                year: car.year ?? 2024,
                baseMsrp: car.baseMsrp ?? 0,
                manufacturerName: manufacturerName ?? "Unknown Make",
                carImageBase64: car.carImageBase64 ?? "images/null.png",
                carImagePath: car.carImagePath,
            );
          }).toList();
        }

        emit(GetCarCardLoadedState(uiCars));
      } catch (e) {
        emit(GetCarCardErrorState(e.toString()));
        if (kDebugMode) {
          print(e);
        }
      }
    });

    on<LoadOrderEvent>((event, emit) async {
      emit(GetCarCardLoadingState());

      try {
        int valueOrder = event.order;
        late final List<CarCardWidget> uiCars;

        if (valueOrder == 4) {
          final List<GetCarsResponse>? getCarsResponse = await Api.getCars();

          if (getCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: car.manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carPath,
            );
          }).toList();
        } else if(valueOrder == 0){
          final List<GetManufacturersCarResponse>? getSortedCarsResponse = await Api.getManufacturerCarsYearDescending(valueManufacturerId);

          if(getSortedCarsResponse == null){
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getSortedCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carImagePath,
            );
          }).toList();
        }else if(valueOrder == 1) {
          final List<
              GetManufacturersCarResponse>? getSortedCarsResponse = await Api
              .getManufacturerCarsYearAscending(valueManufacturerId);

          if (getSortedCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getSortedCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carImagePath,
            );
          }).toList();
        } else if(valueOrder == 2) {
          final List<
              GetManufacturersCarResponse>? getSortedCarsResponse = await Api
              .getManufacturerCarsMSRPDescending(valueManufacturerId);

          if (getSortedCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getSortedCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carImagePath,
            );
          }).toList();
        } else if(valueOrder == 3) {
          final List<
              GetManufacturersCarResponse>? getSortedCarsResponse = await Api
              .getManufacturerCarsMSRPAscending(valueManufacturerId);

          if (getSortedCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getSortedCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carImagePath,
            );
          }).toList();
        }

        emit(GetCarCardLoadedState(uiCars));
      } catch (e) {
        emit(GetCarCardErrorState(e.toString()));
        if (kDebugMode) {
          print(e);
        }
      }
    });

    on<LoadDeleteCar>((event, emit) async{
      emit(GetCarCardLoadingState());


      try{
        late final List<CarCardWidget> uiCars;
        final int? statusCode = await Api.deleteCar(event.carId);

        if (statusCode == 200) {
          final List<GetCarsResponse>? getCarsResponse = await Api.getCars();

          if (getCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: car.manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carPath,
            );
          }).toList();
        }

        emit(GetCarCardLoadedState(uiCars));
      } catch (e) {
        emit(GetCarCardErrorState(e.toString()));
        if (kDebugMode) {
          print(e);
        }
      }
    });

    on<LoadEditCar>((event, emit) async {
      emit(GetCarCardLoadingState());

      try{
        late final List<CarCardWidget> uiCars;

        final int? statusCode = await Api.editCar(
            event.carId,
            event.model,
            event.year,
            event.baseMsrp,
            event.manufacturerId
        );

        if (statusCode == 200) {
          final List<GetCarsResponse>? getCarsResponse = await Api.getCars();

          if (getCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: car.manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carPath,
            );
          }).toList();

          emit(GetCarCardLoadedState(uiCars));
        }
      } catch (e) {
        emit(GetCarCardErrorState(e.toString()));
        if (kDebugMode) {
          print(e);
        }
      }
    });

    on<LoadAddCar>((event, emit) async {
      emit(GetCarCardLoadingState());


      try {
        late final List<CarCardWidget> uiCars;
        final int? statusCode = await Api.addCar(event.model, event.year, event.baseMsrp, event.manufacturerId, event.imagePath);

        if (statusCode == 200) {
          final List<GetCarsResponse>? getCarsResponse = await Api.getCars();

          if (getCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getCarsResponse.map((car) {
            return CarCardWidget(
              carId: car.carId,
              model: car.model ?? "Unknown Model",
              year: car.year ?? 2024,
              baseMsrp: car.baseMsrp ?? 0,
              manufacturerName: car.manufacturerName ?? "Unknown Make",
              carImageBase64: car.carImageBase64 ?? "",
              carImagePath: car.carPath,
            );
          }).toList();
        }

        emit(GetCarCardLoadedState(uiCars));
      } catch (e) {
        emit(GetCarCardErrorState(e.toString()));
        if (kDebugMode) {
          print(e);
        }
      }
    });
  }
}