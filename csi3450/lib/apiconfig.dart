class AppConfig {
  static const String ip = "127.0.0.1:8000";

  static final Endpoint insertManufacturer = Endpoint(ip: ip, link: "api/insert_manufacturer");
  static final Endpoint insertCar = Endpoint(ip: ip, link: "api/insert_car");

  //missing images, because wtf is that shit

  static final Endpoint getManufacturers = Endpoint(ip: ip, link: "api/get_manufacturers");
  static final Endpoint getCars = Endpoint(ip: ip, link: "api/get_cars");

  ///Needs a id value at the end
  static final Endpoint getManufacturersCars = Endpoint(ip: ip, link: "api/get_manufacturer_cars/");
  static final Endpoint getManufacturersId = Endpoint(ip: ip, link: "api/get_manufacturers/");

  static final Endpoint editManufacturer = Endpoint(ip: ip, link: "api/edit_manufacturer");
  static final Endpoint editCar = Endpoint(ip: ip, link: "api/edit_car");

  static final Endpoint deleteCar = Endpoint(ip: ip, link: "api/delete_car/");
}

///Holds an API endpoint with IP and link path.
class Endpoint {
  String ip;
  String link;

  /// Returns the full URL in the format `ip/link`.
  Endpoint({
    required this.ip,
    required this.link,
  });
}