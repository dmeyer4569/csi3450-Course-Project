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
  String carImagePath;

  GetManufacturersCarResponse({
    required this.carId,
    required this.model,
    required this.year,
    required this.baseMsrp,
    required this.carImageId,
    required this.role,
    required this.addedAt,
    required this.carImageBase64,
    required this.carImagePath,
  });

  factory GetManufacturersCarResponse.fromJson(Map<String, dynamic> json) => GetManufacturersCarResponse(
    carId: json["carID"] ?? 0,
    model: json["model"] ?? "Unknown Model",
    year: json["year"] ?? 0,
    baseMsrp: json["baseMSRP"] ?? 0,
    carImageId: json["carImageID"] ?? 0,
    role: json["role"] ?? "logo",
    addedAt: json["addedAt"] == null
        ? DateTime.now()
        : (DateTime.tryParse(json["addedAt"]) ?? DateTime.now()),

    carImagePath: json["FilePath"] ?? "images/null.png",
    carImageBase64: json["manufacturer_logo_path"] ?? "images/null.png",

  );

  Map<String, dynamic> toJson() => {
    "carID": carId,
    "model": model,
    "year": year,
    "baseMSRP": baseMsrp,
    "carImageID": carImageId,
    "role": role,
    "addedAt": addedAt.toIso8601String(),
    "car_image_path": carImageBase64,
  };
}
