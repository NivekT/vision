# TODO: Add _log_api_usage_once() in all mid-level kernels. If they remain not jit-scriptable we can use decorators

from torchvision.transforms import InterpolationMode  # usort: skip
from ._meta import (
    clamp_bounding_box,
    convert_bounding_box_format,
    convert_color_space_image_tensor,
    convert_color_space_image_pil,
    convert_color_space,
    get_dimensions,
    get_image_num_channels,
    get_image_size,
)  # usort: skip

from ._augment import erase, erase_image_pil, erase_image_tensor
from ._color import (
    adjust_brightness,
    adjust_brightness_image_pil,
    adjust_brightness_image_tensor,
    adjust_contrast,
    adjust_contrast_image_pil,
    adjust_contrast_image_tensor,
    adjust_gamma,
    adjust_gamma_image_pil,
    adjust_gamma_image_tensor,
    adjust_hue,
    adjust_hue_image_pil,
    adjust_hue_image_tensor,
    adjust_saturation,
    adjust_saturation_image_pil,
    adjust_saturation_image_tensor,
    adjust_sharpness,
    adjust_sharpness_image_pil,
    adjust_sharpness_image_tensor,
    autocontrast,
    autocontrast_image_pil,
    autocontrast_image_tensor,
    equalize,
    equalize_image_pil,
    equalize_image_tensor,
    invert,
    invert_image_pil,
    invert_image_tensor,
    posterize,
    posterize_image_pil,
    posterize_image_tensor,
    solarize,
    solarize_image_pil,
    solarize_image_tensor,
)
from ._geometry import (
    affine,
    affine_bounding_box,
    affine_image_pil,
    affine_image_tensor,
    affine_segmentation_mask,
    center_crop,
    center_crop_bounding_box,
    center_crop_image_pil,
    center_crop_image_tensor,
    center_crop_segmentation_mask,
    crop,
    crop_bounding_box,
    crop_image_pil,
    crop_image_tensor,
    crop_segmentation_mask,
    elastic,
    elastic_bounding_box,
    elastic_image_pil,
    elastic_image_tensor,
    elastic_segmentation_mask,
    elastic_transform,
    five_crop,
    five_crop_image_pil,
    five_crop_image_tensor,
    hflip,
    horizontal_flip,
    horizontal_flip_bounding_box,
    horizontal_flip_image_pil,
    horizontal_flip_image_tensor,
    horizontal_flip_segmentation_mask,
    pad,
    pad_bounding_box,
    pad_image_pil,
    pad_image_tensor,
    pad_segmentation_mask,
    perspective,
    perspective_bounding_box,
    perspective_image_pil,
    perspective_image_tensor,
    perspective_segmentation_mask,
    resize,
    resize_bounding_box,
    resize_image_pil,
    resize_image_tensor,
    resize_segmentation_mask,
    resized_crop,
    resized_crop_bounding_box,
    resized_crop_image_pil,
    resized_crop_image_tensor,
    resized_crop_segmentation_mask,
    rotate,
    rotate_bounding_box,
    rotate_image_pil,
    rotate_image_tensor,
    rotate_segmentation_mask,
    ten_crop,
    ten_crop_image_pil,
    ten_crop_image_tensor,
    vertical_flip,
    vertical_flip_bounding_box,
    vertical_flip_image_pil,
    vertical_flip_image_tensor,
    vertical_flip_segmentation_mask,
    vflip,
)
from ._misc import gaussian_blur, gaussian_blur_image_pil, gaussian_blur_image_tensor, normalize, normalize_image_tensor
from ._type_conversion import (
    convert_image_dtype,
    decode_image_with_pil,
    decode_video_with_av,
    pil_to_tensor,
    to_image_pil,
    to_image_tensor,
    to_pil_image,
)

from ._deprecated import rgb_to_grayscale, to_grayscale  # usort: skip
