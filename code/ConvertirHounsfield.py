{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b583c82-59bd-4427-962e-e5c3f0cc0c19",
   "metadata": {},
   "outputs": [],
   "source": [
    "def convertir_Hounsfield(lista_datasets):\n",
    "        \n",
    "    lista_H = [] \n",
    "    for ds in lista_datasets:\n",
    "        b = ds.RescaleIntercept\n",
    "        m = ds.RescaleSlope\n",
    "        SV = ds.pixel_array\n",
    "\n",
    "        ValorHounsfield = m*SV + b\n",
    "        lista_H.append(ValorHounsfield)\n",
    "    \n",
    "    return lista_H"
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
