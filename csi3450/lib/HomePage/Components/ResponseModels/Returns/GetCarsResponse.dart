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
  String carPath;

  GetCarsResponse({
    required this.carId,
    required this.model,
    required this.year,
    required this.baseMsrp,
    required this.role,
    required this.manufacturerName,
    required this.carImageBase64,
    required this.carPath
  });

  factory GetCarsResponse.fromJson(Map<String, dynamic> json) => GetCarsResponse(
    carId: json["carID"] ?? 0,
    model: json["model"] ?? "Unknown Model",
    year: json["year"] ?? 0,
    baseMsrp: json["baseMSRP"] ?? 0,
    role: roleValues.map[json["role"]] ?? Role.LOGO,
    manufacturerName: json["manufacturerName"] ?? "Unknown Manufacturer",
    carImageBase64: json["manufacturer_logo_path"] ?? "images/null.png",
    carPath: json["car_image_path"] ?? "images/null.png"
  );

  Map<String, dynamic> toJson() => {
    "carID": carId,
    "model": model,
    "year": year,
    "baseMSRP": baseMsrp,
    "role": roleValues.reverse[role],
    "manufacturerName": manufacturerName,
    "manufacturer_logo_path": carImageBase64,
    "car_image_path": carPath
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