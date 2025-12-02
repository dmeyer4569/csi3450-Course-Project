// To parse this JSON data, do
//
//     final getManufacturersCarResponse = getManufacturersCarResponseFromJson(jsonString);

import 'dart:convert';

List<GetManufacturersCarResponse> getManufacturersCarResponseFromJson(String str) => List<GetManufacturersCarResponse>.from(json.decode(str).map((x) => GetManufacturersCarResponse.fromJson(x)));

String getManufacturersCarResponseToJson(List<GetManufacturersCarResponse> data) => json.encode(List<dynamic>.from(data.map((x) => x.toJson())));

class GetManufacturersCarResponse {
  int carId;
  String model;
  int year;
  int baseMsrp;
  int carImageId;
  String role;
  DateTime addedAt;
  String carImageBase64;

  GetManufacturersCarResponse({
    required this.carId,
    required this.model,
    required this.year,
    required this.baseMsrp,
    required this.carImageId,
    required this.role,
    required this.addedAt,
    required this.carImageBase64,
  });

  factory GetManufacturersCarResponse.fromJson(Map<String, dynamic> json) => GetManufacturersCarResponse(
    carId: json["carID"],
    model: json["model"],
    year: json["year"],
    baseMsrp: json["baseMSRP"],
    carImageId: json["carImageID"],
    role: json["role"],
    addedAt: DateTime.parse(json["addedAt"]),
    carImageBase64: json["car_image_base64"],
  );

  Map<String, dynamic> toJson() => {
    "carID": carId,
    "model": model,
    "year": year,
    "baseMSRP": baseMsrp,
    "carImageID": carImageId,
    "role": role,
    "addedAt": addedAt.toIso8601String(),
    "car_image_base64": carImageBase64,
  };
}
