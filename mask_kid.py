from detect import run
run_dict = {
    'weights': 'best.pt',
    'source': 0,
    'imgsz': [640, 640],
    'conf_thres': 0.70,
    'iou_thres': 0.60,
    'max_det': 10,
    'device': '0',
    'view_img': False,
    'save_txt': False,
    'save_conf': False,
    'save_crop': False,
    'nosave': False,
    'classes': None,
    'agnostic_nms': False,
    'augment': False,
    'visualize': False,
    'update': False,
    'project': 'runs/detect',
    'name': 'exp',
    'exist_ok': False,
    'line_thickness': 3,
    'hide_labels': False,
    'hide_conf': False,
    'half': False,
}

run(**run_dict)
