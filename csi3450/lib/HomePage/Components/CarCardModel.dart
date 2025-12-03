import 'dart:convert';
import 'dart:io';
import 'dart:typed_data';
import 'dart:ui';
import 'package:csi3450/HomePage/Components/getCarBloC/get_car_card_bloc.dart';
import 'package:smooth_page_indicator/smooth_page_indicator.dart'
    as smooth_page_indicator;
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

import 'CarCardModel.dart';
import 'EditCarDialogModel.dart';
export 'CarCardModel.dart';

class CarCardWidget extends StatefulWidget {
  final int carId;
  final String model;
  final int year;
  final int baseMsrp;
  final String manufacturerName;
  final String carImageBase64;
  final String carImagePath;

  const CarCardWidget({
    super.key,
    required this.carId,
    required this.model,
    required this.year,
    required this.baseMsrp,
    required this.manufacturerName,
    required this.carImageBase64,
    required this.carImagePath,
  });

  @override
  State<CarCardWidget> createState() => _CarCardWidgetState();
}

class _CarCardWidgetState extends State<CarCardWidget> {
  // late Uint8List _imageBytes;

  void initState() {
    super.initState();
    // _imageBytes = base64Decode(widget.carImageBase64);
  }

  @override
  Widget build(BuildContext context) {
    return Align(
      alignment: AlignmentDirectional(0, 0),
      child: Container(
        width: 200,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.only(
            bottomLeft: Radius.circular(0),
            bottomRight: Radius.circular(0),
            topLeft: Radius.circular(0),
            topRight: Radius.circular(0),
          ),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.max,
          children: [
            Card(
              clipBehavior: Clip.antiAliasWithSaveLayer,
              // color: FlutterFlowTheme.of(context).secondaryBackground,
              elevation: 0,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              ),
              child: Column(
                mainAxisSize: MainAxisSize.max,
                children: [
                  SizedBox(
                    height: 200,
                    child: Align(
                      alignment: AlignmentDirectional(0, -1),
                      child: Container(
                        width: MediaQuery.sizeOf(context).width,
                        height: MediaQuery.sizeOf(context).height,
                        decoration: BoxDecoration(
                          // color: FlutterFlowTheme.of(context)
                          //     .secondaryBackground,
                          borderRadius: BorderRadius.only(
                            bottomLeft: Radius.circular(0),
                            bottomRight: Radius.circular(0),
                            topLeft: Radius.circular(0),
                            topRight: Radius.circular(0),
                          ),
                        ),
                        child: Stack(
                          children: [
                            Container(
                              width: double.infinity,
                              height: 500,
                              child: Stack(
                                children: [
                                  ClipRRect(
                                    borderRadius: BorderRadius.only(
                                      bottomLeft: Radius.circular(0),
                                      bottomRight: Radius.circular(0),
                                      topLeft: Radius.circular(0),
                                      topRight: Radius.circular(0),
                                    ),
                                    child: Image.network(
                                      "http://127.0.0.1:8000/${widget.carImagePath}",
                                      width: 200,
                                      height: MediaQuery.sizeOf(context).height,
                                      fit: BoxFit.fill,
                                      alignment: Alignment(0, -1),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            Opacity(
                              opacity: 0.6,
                              child: Container(
                                width: double.infinity,
                                height: double.infinity,
                                decoration: BoxDecoration(
                                  gradient: LinearGradient(
                                    colors: [Colors.black, Colors.transparent],
                                    stops: [0, 1],
                                    begin: AlignmentDirectional(0, -1),
                                    end: AlignmentDirectional(0, 1),
                                  ),
                                ),
                                alignment: AlignmentDirectional(0, -1),
                              ),
                            ),
                            Row(
                              mainAxisSize: MainAxisSize.min,
                              mainAxisAlignment: MainAxisAlignment.start,
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Flexible(
                                  child: Align(
                                    alignment: AlignmentDirectional(-1, -1),
                                    child: Padding(
                                      padding: EdgeInsetsDirectional.fromSTEB(
                                        10,
                                        10,
                                        10,
                                        10,
                                      ),
                                      child: Text(
                                        widget.model,
                                        style: GoogleFonts.inter(
                                          fontWeight: FontWeight.bold,
                                          color: Colors.white,
                                          fontSize: 19,
                                          letterSpacing: 0.0,
                                        ),
                                      ),
                                    ),
                                  ),
                                ),
                                Align(
                                  alignment: AlignmentDirectional(1, -1),
                                  child: Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                      10,
                                      10,
                                      10,
                                      10,
                                    ),
                                    child: Text(
                                      widget.year.toString(),
                                      style: GoogleFonts.inter(
                                        fontWeight: FontWeight.bold,
                                        color: Colors.white,
                                        fontSize: 19,
                                        letterSpacing: 0.0,
                                      ),
                                    ),
                                  ),
                                ),
                              ],
                            ),
                            // --- NEW CODE STARTS HERE ---
                            Align(
                              alignment: AlignmentDirectional(1, 1),
                              child: Padding(
                                padding: const EdgeInsets.all(8.0),
                                child: Container(
                                  decoration: BoxDecoration(
                                    color: Colors.black.withOpacity(0.4),
                                    borderRadius: BorderRadius.circular(20),
                                  ),
                                  child: Row(
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                      IconButton(
                                        visualDensity: VisualDensity.compact,
                                        icon: const Icon(
                                          Icons.edit,
                                          color: Colors.white,
                                          size: 20,
                                        ),
                                        onPressed: () {
                                          // Add your Edit logic here
                                          EditCarDialog.show(
                                            context,
                                            carId: widget.carId,
                                            currentModel: widget.model,
                                            currentYear: widget.year,
                                            currentBaseMsrp: widget.baseMsrp,
                                            currentManufacturerName: widget.manufacturerName,
                                          );
                                        },
                                      ),
                                      IconButton(
                                        visualDensity: VisualDensity.compact,
                                        icon: const Icon(
                                          Icons.delete,
                                          color: Colors.redAccent,
                                          size: 20,
                                        ),
                                        onPressed: () {
                                          context.read<GetCarCardBloc>().add(
                                            LoadDeleteCar(carId: widget.carId),
                                          );
                                        },
                                      ),
                                    ],
                                  ),
                                ),
                              ),
                            ),
                            // --- NEW CODE ENDS HERE ---
                          ],
                        ),
                      ),
                    ),
                  ),
                  Align(
                    alignment: AlignmentDirectional(0, 1),
                    child: Container(
                      width: 300,
                      height: 60,
                      decoration: BoxDecoration(
                        // color: FlutterFlowTheme.of(context)
                        //     .secondaryBackground,
                      ),
                      child: Padding(
                        padding: EdgeInsetsDirectional.fromSTEB(1, 0, 0, 0),
                        child: Row(
                          mainAxisSize: MainAxisSize.max,
                          children: [
                            Flexible(
                              child: Padding(
                                padding: EdgeInsetsDirectional.fromSTEB(
                                  5,
                                  5,
                                  5,
                                  5,
                                ),
                                child: Container(
                                  width: 50,
                                  clipBehavior: Clip.antiAlias,
                                  decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                  ),
                                  child: Image.network(
                                    //here, it would be better to pass a file instead, but yknow what, it is what it is.
                                    "http://127.0.0.1:8000/${widget.carImageBase64}",
                                    fit: BoxFit.contain,
                                  ),
                                ),
                              ),
                            ),
                            Column(
                              mainAxisSize: MainAxisSize.max,
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Align(
                                  alignment: AlignmentDirectional(-1, 0),
                                  child: Padding(
                                    padding: EdgeInsetsDirectional.fromSTEB(
                                      0,
                                      3,
                                      0,
                                      0,
                                    ),
                                    child: Text(
                                      widget.manufacturerName,
                                      style: GoogleFonts.inter(
                                        fontWeight: FontWeight.w600,
                                        fontSize: 13,
                                        letterSpacing: 0.0,
                                      ),
                                    ),
                                  ),
                                ),
                                Align(
                                  alignment: AlignmentDirectional(-1, 0),
                                  child: Text(
                                    'Estimated retail value:',
                                    style: GoogleFonts.inter(
                                      fontWeight: FontWeight.normal,
                                      color: Color(0xFF9CADB0),
                                      fontSize: 8,
                                      letterSpacing: 0.0,
                                    ),
                                  ),
                                ),
                                Text(
                                  '\$${widget.baseMsrp}',
                                  style: GoogleFonts.inter(
                                    fontWeight: FontWeight.bold,
                                    letterSpacing: 0.0,
                                  ),
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
