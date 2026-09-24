import 'package:flutter/material.dart';
void main()=>runApp(const MathSpaceApp());
class MathSpaceApp extends StatelessWidget{
 const MathSpaceApp({super.key});
 Widget build(BuildContext context)=>MaterialApp(
  title:'MathSpace',theme:ThemeData(colorSchemeSeed:Colors.deepPurple,useMaterial3:true),
  home:Scaffold(appBar:AppBar(title:const Text('MathSpace')),body:const Center(child:Text('AI Mathematics Intelligence Platform')))
 );
}
