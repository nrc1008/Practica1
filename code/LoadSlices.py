{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fafb2295-75ba-4cb5-a03e-f0055cac7164",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Load_Slices(directorio):\n",
    "    archivos=[]\n",
    "    \n",
    "    if directorio is None:\n",
    "        print( \"Directorio no seleccionado\")\n",
    "        return None\n",
    "  \n",
    "    for aname in Path(directorio).rglob(\"*.dcm\"):\n",
    "        print(f\"Loading: {aname}\")\n",
    "        archivos.append(dcm.dcmread(aname))\n",
    "\n",
    "    if not archivos:\n",
    "        print(\" Este directorio no tiene imagenes del formato seleccionado.\")\n",
    "        \n",
    "    return archivos\n"
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
