part of 'get_car_card_bloc.dart';

sealed class GetCarCardState extends Equatable {
  const GetCarCardState();

  @override
  List<Object> get props => [];
}

class GetCarCardInitialState extends GetCarCardState {}

class GetCarCardLoadingState extends GetCarCardState {}

class GetCarCardLoadedState extends GetCarCardState {
  final List<CarCardWidget> carCardModel;

  const GetCarCardLoadedState(this.carCardModel);

  @override
  List<Object> get props => [carCardModel];
}

class GetCarCardErrorState extends GetCarCardState{
  final String message;

  const GetCarCardErrorState(this.message);

  @override
  List<Object> get props => [message];
}