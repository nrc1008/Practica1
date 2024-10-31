{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6bdab68-065c-4252-9c82-28767b3e4637",
   "metadata": {},
   "outputs": [],
   "source": [
    "def MetadataCT(imagenes):\n",
    "\n",
    "    if not imagenes:\n",
    "        print(\"No hay imagenes DICOM.\")\n",
    "        return \n",
    "         \n",
    "    imagen = imagenes[0]\n",
    "\n",
    "    nombre_sujeto = imagen.get(\"PatientName\", \"Desconocido\")\n",
    "    edad_sujeto = imagen.get(\"PatientAge\", \"Desconocido\")\n",
    "    sexo_sujeto = imagen.get(\"PatientSex\", \"Desconocido\")\n",
    "    tipo_imagen = imagen.get(\"Modality\", \"Desconocido\")\n",
    "    fecha_adquisicion = imagen.get(\"AcquisitionDate\", \"Desconocido\")\n",
    "    modelo_tomografo = imagen.get(\"ManufacturerModelName\", \"Desconocido\")\n",
    "    tipo_adquisicion = imagen.get(\"SequenceName\", \"Desconocido\")\n",
    "\n",
    "    #Tamaño del vóxel\n",
    "    ps = imagen.PixelSpacing\n",
    "    ss = imagen.SliceThickness\n",
    "    tamaño_voxel = (ps[1], ps[0], ss)  #(alto, ancho, espaciado)\n",
    "\n",
    "    #Tamaño imagen\n",
    "    alto = imagen.Rows\n",
    "    ancho = imagen.Columns\n",
    "    numero_imagenes=len(imagenes)\n",
    "    tamaño_imagen_mm=(alto*ps[1], ancho*ps[0], numero_imagenes*ss)\n",
    "    tamaño_imagen_voxeles=(alto, ancho, numero_imagenes)\n",
    "\n",
    "    print(f\"Nombre del sujeto: {nombre_sujeto}\")\n",
    "    print(f\"Edad del sujeto: {edad_sujeto}\")\n",
    "    print(f\"Sexo del sujeto: {sexo_sujeto}\")\n",
    "    print(f\"Tipo de imagen: {tipo_imagen}\")\n",
    "    print(f\"Fecha de adquisición: {fecha_adquisicion}\")\n",
    "    print(f\"Modelo de tomógrafo en la que se realizó la prueba de imagen: {modelo_tomografo}\")    \n",
    "    print(f\"Tipo de adquisición (corte): {tipo_adquisicion}\")\n",
    "    print(f\"Tamaño del vóxel : {tamaño_voxel}\")\n",
    "    print(f\"Tamaño de la imagen en mm: {tamaño_imagen_mm} mm\")\n",
    "    print(f\"Tamaño de la imagen en voxeles: {tamaño_imagen_voxeles}\")\n",
    "\n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.20"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
