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

class LoadAddCar extends GetCarCardEvent {
  final String model;
  final int year;
  final int baseMsrp;
  final int manufacturerId;
  final String imagePath;

  const LoadAddCar({
    required this.model,
    required this.year,
    required this.baseMsrp,
    required this.manufacturerId,
    required this.imagePath
  });

  List<Object> get props => [
    model ?? "unknown model",
    year ?? 0,
    baseMsrp ?? 9999999999,
    manufacturerId ?? 1,
    imagePath ?? "images/null.png"
  ];
}