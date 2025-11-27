part of 'get_car_card_bloc.dart';

sealed class GetCarCardEvent extends Equatable {
  const GetCarCardEvent();

  @override
  List<Object> get props => [];
}

class LoadCarsEvent extends GetCarCardEvent {}