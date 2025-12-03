part of 'get_car_card_bloc.dart';

sealed class GetCarCardEvent extends Equatable {
  const GetCarCardEvent();

  @override
  List<Object> get props => [];
}

class LoadCarsEvent extends GetCarCardEvent {
  final int manufacturerId;
  final String manufacturerName;

  const LoadCarsEvent({
    required this.manufacturerId,
    required this.manufacturerName,
  });

  @override
  List<Object> get props => [manufacturerId ?? 0, manufacturerName ?? "Null"];
}

class LoadOrderEvent extends GetCarCardEvent {
  final int order;

  const LoadOrderEvent({
    required this.order
  });

  @override
  List<Object> get props => [order ?? 0];
}

class LoadDeleteCar extends GetCarCardEvent{
  final int carId;

  const LoadDeleteCar({
    required this.carId
  });

  @override
  List<Object> get props => [carId ?? 1];
}

class LoadEditCar extends GetCarCardEvent {
  final int carId;
  final String model;
  final int year;
  final int baseMsrp;
  final int manufacturerId;

  const LoadEditCar({
    required this.carId,
    required this.model,
    required this.year,
    required this.baseMsrp,
    required this.manufacturerId
  });

  @override
  List<Object> get props => [
    carId ?? 1,
    model ?? "bootyahhcar",
    year ?? 1,
    baseMsrp ?? 1,
    manufacturerId ?? 1,
  ];
}