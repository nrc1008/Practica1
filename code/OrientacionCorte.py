{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31c8949e-92b5-41f2-8417-c1c1e0f113d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def OrientacionCorte (lista_datasets):\n",
    "    #import numpy as np\n",
    "    iop=lista_datasets.ImageOrientationPatient\n",
    "    iop_rounded = [round(x) for x in iop]\n",
    "    plane_cross = np.cross(iop_rounded[0:3], iop_rounded[3:6])\n",
    "    plane = [abs(x) for x in plane_cross]\n",
    "    if plane[0] == 1:\n",
    "        return 'Sagital'\n",
    "    elif plane[1] == 1:\n",
    "        return 'Coronal'\n",
    "    elif plane[2] == 1:\n",
    "        return 'Axial'\n",
    "    else:\n",
    "        return 'NA'"
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
