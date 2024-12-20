{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2560321c-ab79-42cb-b846-2c2464f5de2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def CrearVolumen(lista_datasets):\n",
    "    if not lista_datasets:\n",
    "        print(\"No hay imagenes DICOM.\")\n",
    "        return\n",
    "\n",
    "\n",
    "    #Unicamente cargamos aquellos archivos DICOM que contengan el campo ImagePositionPatient en la lista denominada slices\n",
    "    slices = []\n",
    "    skipcount = 0\n",
    "    for ds in lista_datasets:\n",
    "        if hasattr(ds, \"ImagePositionPatient\"):\n",
    "            slices.append(ds)\n",
    "        else:\n",
    "            skipcount = skipcount + 1\n",
    "\n",
    "    print(f\"Se han descartado {skipcount} archivos\")\n",
    "\n",
    "    if not slices:\n",
    "        print(\"No se encontraron imágenes DICOM válidas con el atributo ImagePositionPatient.\")\n",
    "        return None\n",
    "\n",
    "    \n",
    "    # Ordenamos los cortes que se encuentran en la lista slices de acuerdo al campo ImagePositionPatient\n",
    "    img_orient=OrientacionCorte (slices[0])\n",
    "    if img_orient == 'Axial':\n",
    "        slices = sorted(slices, key=lambda s: s.ImagePositionPatient[2])\n",
    "\n",
    "    elif img_orient == 'Coronal':\n",
    "        slices = sorted(slices, key=lambda s: s.ImagePositionPatient[1])\n",
    "\n",
    "    elif img_orient == 'Sagital':\n",
    "        slices = sorted(slices, key=lambda s: s.ImagePositionPatient[0])\n",
    "\n",
    "    else:\n",
    "        slices = []\n",
    "\n",
    "    slices_H = convertir_Hounsfield(slices)\n",
    "    \n",
    "    ps = slices[0].PixelSpacing    #array bidimensional que contiene el tamaño de pixel en mm del corte.\n",
    "    ss = slices[0].SliceThickness  #distancia en mm entre el corte almacenado del archivo y el inmediatamente anterior (o posterior)\n",
    "    \n",
    "    if img_orient == 'Axial':\n",
    "        img_shape = list(slices[0].pixel_array.shape)\n",
    "        img_shape.append(len(slices))\n",
    "        img3d = np.zeros(img_shape)\n",
    "        for i, s in enumerate(slices_H):\n",
    "            img3d[:, :, len(slices)-i-1] = s\n",
    "        ax_aspect = ps[0] / ps[1]\n",
    "        sag_aspect = ss /ps[1]\n",
    "        cor_aspect = ss /ps[0]\n",
    "        voxel_size=[ps[0],ps[1],ss]\n",
    "    \n",
    "    elif img_orient =='Coronal':\n",
    "        img_shape=[]\n",
    "        img_shape.append(len(slices))\n",
    "        img_shape.append(slices[0].pixel_array.shape[0])\n",
    "        img_shape.append(slices[0].pixel_array.shape[1])\n",
    "        img3d = np.zeros(img_shape)\n",
    "        for i, s in enumerate(slices_H):\n",
    "            img3d[i, :, :] = s.T\n",
    "        ax_aspect = ss / ps[1]\n",
    "        sag_aspect = ps[0] /ss\n",
    "        cor_aspect = ps[0] / ps[1]\n",
    "        voxel_size=[ps[0],ss, ps[1]]\n",
    "    \n",
    "    elif img_orient =='Sagital':\n",
    "        img_shape=[]\n",
    "        img_shape.append(slices[0].pixel_array.shape[0])\n",
    "        img_shape.append(len(slices))    \n",
    "        img_shape.append(slices[0].pixel_array.shape[1])\n",
    "        img3d = np.zeros(img_shape)\n",
    "        for i, s in enumerate(slices_H):\n",
    "            img3d[:, len(slices)-i-1, :] = s.T\n",
    "        ax_aspect = ps[0] /ss\n",
    "        sag_aspect = ps[1] /ps[0] \n",
    "        cor_aspect = ps[1] /ss\n",
    "        voxel_size=[ss, ps[0], ps[1]]\n",
    "    else:\n",
    "        print(\"Error en la obtención de la vista\")\n",
    "\n",
    "    \n",
    "    relacion_aspecto = [ax_aspect, sag_aspect, cor_aspect]\n",
    "    \n",
    "    return img3d, img_shape, relacion_aspecto, voxel_size"
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
