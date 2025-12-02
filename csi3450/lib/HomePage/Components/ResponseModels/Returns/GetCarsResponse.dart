import 'dart:convert';

List<GetCarsResponse> getCarsResponseFromJson(String str) => List<GetCarsResponse>.from(json.decode(str).map((x) => GetCarsResponse.fromJson(x)));

String getCarsResponseToJson(List<GetCarsResponse> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class GetCarsResponse {
  int carId;
  String model;
  int year;
  int baseMsrp;
  Role role;
  String manufacturerName;
  String carImageBase64;

  GetCarsResponse({
    required this.carId,
    required this.model,
    required this.year,
    required this.baseMsrp,
    required this.role,
    required this.manufacturerName,
    required this.carImageBase64,
  });

  factory GetCarsResponse.fromJson(Map<String, dynamic> json) => GetCarsResponse(
    carId: json["carID"],
    model: json["model"],
    year: json["year"],
    baseMsrp: json["baseMSRP"],
    role: roleValues.map[json["role"]]!,
    manufacturerName: json["manufacturerName"],
    carImageBase64: json["car_image_base64"],
  );

  Map<String, dynamic> toJson() => {
    "carID": carId,
    "model": model,
    "year": year,
    "baseMSRP": baseMsrp,
    "role": roleValues.reverse[role],
    "manufacturerName": manufacturerName,
    "car_image_base64": carImageBase64,
  };
}

enum Role {
  LOGO
}

final roleValues = EnumValues({
  "logo": Role.LOGO
});

class EnumValues<T> {
  Map<String, T> map;
  late Map<T, String> reverseMap;

  EnumValues(this.map);

  Map<T, String> get reverse {
    reverseMap = map.map((k, v) => MapEntry(v, k));
    return reverseMap;
  }
}
