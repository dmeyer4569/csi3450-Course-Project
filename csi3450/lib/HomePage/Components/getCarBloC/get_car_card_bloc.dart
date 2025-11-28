import 'package:bloc/bloc.dart';
import 'package:csi3450/HomePage/Components/ResponseModels/Returns/GetManufacturerCarsResponse.dart';
import 'package:equatable/equatable.dart';

import '../CarCardModel.dart';
import '../ResponseModels/Returns/GetCarsResponse.dart';
import '../ResponseModels/api.dart';

part 'get_car_card_event.dart';
part 'get_car_card_state.dart';

class GetCarCardBloc extends Bloc<GetCarCardEvent, GetCarCardState> {
  GetCarCardBloc() : super(GetCarCardInitialState()) {
    on<LoadCarsEvent>((event, emit) async {
      emit(GetCarCardLoadingState());

      try {
        int value = event.manufacturerId;
        late final List<CarCardWidget> uiCars;

        if (value == 0) {
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
            );
          }).toList();
        } else {
          final List<GetManufacturersCarResponse>? getManufacturersCarsResponse = await Api.getManufacturerCars(value);

          if (getManufacturersCarsResponse == null) {
            emit(const GetCarCardErrorState("Failed to fetch data"));
            return;
          }

          uiCars = getManufacturersCarsResponse.map((car) {
            return CarCardWidget(
                carId: car.carId,
                model: car.model ?? "Unknown Model",
                year: car.year ?? 2024,
                baseMsrp: car.baseMsrp ?? 0,
                manufacturerName: event.manufacturerName ?? "Unknown Make",
                carImageBase64: car.carImageBase64 ?? "",
            );
          }).toList();
        }

        emit(GetCarCardLoadedState(uiCars));
      } catch (e) {
        emit(GetCarCardErrorState(e.toString()));
        print(e);
      }
    });
  }
}
