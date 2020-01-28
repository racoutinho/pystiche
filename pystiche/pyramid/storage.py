from pystiche.ops import ComparisonOperator, Guidance, ComparisonGuidance

__all__ = ["ImageStorage"]


class ImageStorage:
    def __init__(self, ops):
        self.target_guides = {}
        self.target_images = {}
        self.input_guides = {}
        for op in ops:
            if isinstance(op, ComparisonGuidance) and op.has_target_guide:
                self.target_guides[op] = op.target_guide

            if isinstance(op, ComparisonOperator) and op.has_target_image:
                self.target_images[op] = op.target_image

            if isinstance(op, Guidance) and op.has_input_guide:
                self.input_guides[op] = op.input_guide

    def restore(self):
        for op, target_guide in self.target_guides.items():
            op.set_target_guide(target_guide, recalc_repr=False)

        for op, target_image in self.target_images.items():
            op.set_target_image(target_image)

        for op, input_guide in self.input_guides.items():
            op.set_input_guide(input_guide)
