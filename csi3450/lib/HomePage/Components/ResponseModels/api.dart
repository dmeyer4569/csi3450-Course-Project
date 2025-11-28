import 'package:csi3450/HomePage/Components/ResponseModels/Returns/GetManufacturerCarsResponse.dart';
import 'package:http/http.dart' as http;

import 'package:csi3450/apiconfig.dart';

import 'Returns/GetCarsResponse.dart';

class Api{

  static Future<List<GetCarsResponse>?> getCars() async {
    final url = Uri.http(
      AppConfig.getCars.ip,
      AppConfig.getCars.link
    );
    final response = await http.get(
      url,
      headers: {
        "Accept": "application/json"
      },
    );

    if(response.statusCode == 200) {
      return getCarsResponseFromJson(response.body);
    } else {
      return null;
    }
  }

  static Future<List<GetManufacturersCarResponse>?> getManufacturerCars(int manufacturerId) async {
    final url = Uri.http(
      AppConfig.getManufacturersCars.ip,
      AppConfig.getManufacturersCars.link + manufacturerId.toString()
    );
    final response = await http.get(
      url,
      headers: {
        "Accept": "application/json"
      },
    );

    if(response.statusCode == 200) {
      return getManufacturersCarResponseFromJson(response.body);
    } else {
      return null;
    }
  }
}