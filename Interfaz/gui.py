from customtkinter import *
#ventana 4
root = CTk()
root.title("CONDOR")
root._set_appearance_mode("light")
root.geometry("1000x600")
root.resizable(0, 0)
root.config(bg = "light pink")
root.iconbitmap("logo.ico")
#---------------------------VARIABLES---------------------------
hora_llegada = "13:00"
hora_salida = "10:00"
lugar_salida = "Bogotá"
lugar_llegada = "Cartagena"
ida = f"Ida: {lugar_salida} - {lugar_llegada}"
precio = "2.000.000"
fecha = "2024-06-13"
flechita = "-------------------------------------->"
#---------------------------FRAMES---------------------------
frame_viaje = CTkFrame(master=root, 
                       fg_color="white", 
                       bg_color = "light pink", 
                       border_color = "black", 
                       corner_radius = 10, 
                       width = 0.11, 
                       height = 0.065, 
                       border_width = 10
                       )
frame_opciones = CTkFrame(master = root, 
                       fg_color="transparent",
                       bg_color = "light pink",
                       border_color = "brown",  
                       corner_radius = 10, 
                       width = 0.7, 
                       height = 0.2, 
                       border_width = 1.5
                       )
opcion1 = CTkFrame(master = frame_opciones, 
                          bg_color = "light pink",    
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30,
                          fg_color = "beige"
                          )
opcion2 = CTkFrame(master = frame_opciones, 
                          fg_color = "beige",  
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30,
                          bg_color = "light pink"
                          )
opcion3 = CTkFrame(master = frame_opciones,
                          fg_color = "beige",  
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30,
                          bg_color = "light pink"
                          )
opcion4 = CTkFrame(master = frame_opciones,
                          fg_color = "beige",
                          bg_color = "light pink",
                          width = 0.9, 
                          height = 0.2, 
                          corner_radius = 30
                          )
#---------------------------TEXTOS---------------------------
text_viaje = CTkLabel(root, text = ida, 
                      fg_color = "beige", 
                      width = 0.2, 
                      height = 0.065, 
                      text_color = "black", 
                      font = ("roboto", 12), 
                      corner_radius = 10, 
                      bg_color = "light pink",
                      )
text_hora_salida = CTkLabel(master = frame_opciones, 
                            text = hora_salida,
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 18),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_hora_llegada = CTkLabel(master = frame_opciones, 
                            text = hora_llegada,
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 18),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_lugar_salida = CTkLabel(master = frame_opciones, 
                            text = lugar_salida,
                            fg_color = "Beige",
                            text_color = "black",
                            font = ("roboto", 13),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_lugar_llegada = CTkLabel(master = frame_opciones, 
                            text = lugar_llegada,
                            fg_color = "Beige",
                            text_color = "black",
                            font = ("roboto", 13),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_desde = CTkLabel(master = frame_opciones,
                      text = """DESDE:

                         COP $""",
                      fg_color = "beige",
                      text_color = "black",
                      font = ("roboto", 11),
                      width = 0.1,
                      height = 0.3,
                      corner_radius = 10,
                      bg_color = "beige"
                      )
text_precio = CTkLabel(master = frame_opciones,
                        text = precio,
                        fg_color = "beige",
                        text_color = "black",
                        font = ("roboto", 11),
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        bg_color = "beige"
                        )
text_flechita = CTkLabel(master = frame_opciones,
                        text = flechita,
                        fg_color = "beige",
                        text_color = "black",
                        font = ("roboto", 20),
                        width = 0.3,
                        height = 0.3,
                        bg_color = "beige"
                        )
#---------------------------BOTONES---------------------------
boton_eleccion1 = CTkButton(master = frame_opciones,
                            text = "ELEGIR",
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 16),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 30,
                            bg_color = "beige"
                            )
boton_eleccion2 = CTkButton(master = frame_opciones,
                            text = "ELEGIR",
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 16),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 30,
                            bg_color = "beige"
                            )
boton_eleccion3 = CTkButton(master = frame_opciones,
                            text = "ELEGIR",
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 16),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 30,
                            bg_color = "beige"
                            )
boton_eleccion4 = CTkButton(master = frame_opciones,
                            text = "ELEGIR",
                            fg_color = "beige",
                            text_color = "black",
                            font = ("roboto", 16),
                            width = 0.1,
                            height = 0.3,
                            corner_radius = 30,
                            bg_color = "beige"
                            )
boton_dias1 = CTkButton(root,
                         text = f"Fecha: {fecha}",
                         fg_color = "beige",
                         text_color = "black",
                         font = ("roboto", 13),
                         width = 0.16,
                         height = 0.057,
                         corner_radius = 10,
                         bg_color = "beige"
                         )
boton_dias2 = CTkButton(root,
                         text = f"Fecha: {fecha}",
                         fg_color = "beige",
                         text_color = "black",
                         font = ("roboto", 13),
                         width = 0.16,
                         height = 0.057,
                         corner_radius = 10,
                         bg_color = "beige"
                         )
boton_dias3 = CTkButton(root,
                         text = f"Fecha: {fecha}",
                         fg_color = "beige",
                         text_color = "black",
                         font = ("roboto", 13),
                         width = 0.16,
                         height = 0.057,
                         corner_radius = 10,
                         bg_color = "beige"
                         )
boton_dias4 = CTkButton(root,
                         text = f"Fecha: {fecha}",
                         fg_color = "beige",
                         text_color = "black",
                         font = ("roboto", 13),
                         width = 0.16,
                         height = 0.057,
                         corner_radius = 10,
                         bg_color = "beige"
                         )
boton_dias5 = CTkButton(root,
                         text = f"Fecha: {fecha}",
                         fg_color = "beige",
                         text_color = "black",
                         font = ("roboto", 13),
                         width = 0.16,
                         height = 0.057,
                         corner_radius = 10,
                         bg_color = "beige"
                         )
#---------------------------POSICIONAMIENTO-----------------------
frame_viaje.place(x = 6, y = 5, relwidth = 0.1, relheight = 0.065)
text_viaje.place(x = 6, y = 5, relwidth = 0.2, relheight = 0.065)
boton_dias1.place(x = 20, y = 74, relwidth = 0.16, relheight = 0.057)
boton_dias2.place(x = 220, y = 74, relwidth = 0.16, relheight = 0.057)
boton_dias3.place(x = 420, y = 74, relwidth = 0.16, relheight = 0.057)
boton_dias4.place(x = 620, y = 74, relwidth = 0.16, relheight = 0.057)
boton_dias5.place(x = 820, y = 74, relwidth = 0.16, relheight = 0.057)
frame_opciones.place(x = 48.35, y = 135, relwidth = 0.9, relheight = 0.7)
opcion1.place(x = 46.6, y = 22.4, relwidth = 0.8, relheight = 0.21)
opcion2.place(x = 46.6, y = 119.4, relwidth = 0.8, relheight = 0.21)
opcion3.place(x = 46.6, y = 216.4, relwidth = 0.8, relheight = 0.21)
opcion4.place(x = 46.6, y = 313.4, relwidth = 0.8, relheight = 0.21)
text_hora_salida.place(x = 70, y = 45, relwidth = 0.08, relheight = 0.057)
text_lugar_salida.place(x = 70, y = 70, relwidth = 0.08, relheight = 0.057)
text_hora_llegada.place(x = 400, y = 45, relwidth = 0.08, relheight = 0.057)
text_lugar_llegada.place(x = 400, y = 70, relwidth = 0.08, relheight = 0.057)
text_desde.place(x = 480, y = 35, relwidth = 0.19, relheight = 0.15)
text_precio.place(x = 620, y = 68, relwidth = 0.08, relheight = 0.057)
text_flechita.place(x = 156, y = 42, relwidth = 0.265, relheight = 0.1)
boton_eleccion1.place(x = 795, y = 50, relwidth = 0.08, relheight = 0.057)
boton_eleccion2.place(x = 795, y = 150, relwidth = 0.08, relheight = 0.057)
boton_eleccion3.place(x = 795, y = 250, relwidth = 0.08, relheight = 0.057)
boton_eleccion4.place(x = 795, y = 350, relwidth = 0.08, relheight = 0.057)
root.mainloop()