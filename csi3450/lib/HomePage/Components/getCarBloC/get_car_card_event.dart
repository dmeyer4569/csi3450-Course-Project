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
    required this.manufacturerName
  });

  @override
  List<Object> get props => [manufacturerId ?? 0, manufacturerName ?? "Null"];
}