import os
import torch
import numpy as np
import onnxruntime as ort

from tmbed.tmbed import load_models


def export_tmbed_to_onnx():
    export_dir = "cnn_onnx"
    if not os.path.exists(export_dir):
        os.mkdir(export_dir)

    models = load_models()

    for index, single_tmbed_model in enumerate(models):
        single_tmbed_model.eval()
        single_tmbed_model.to("cpu")

        # Define the dummy input tensor `x` and mask tensor `mask`
        # Use a reasonable sequence length for testing
        B = 1  # batch size
        N = 32  # sequence length (can be any reasonable number)
        C = 1024  # number of input channels/features

        x = torch.randn(B, N, C)
        mask = torch.ones(B, N)

        specific_onnx_file_path = f'{export_dir}/cv_{index}.onnx'

        # Export the model with dynamic axes
        torch.onnx.export(
            single_tmbed_model,
            (x, mask),
            specific_onnx_file_path,
            export_params=True,
            opset_version=14,
            do_constant_folding=True,
            input_names=['input', 'mask'],
            output_names=['output'],
            dynamic_axes={
                'input': {0: 'batch_size', 1: 'sequence_length'},  # dynamic axes
                'mask': {0: 'batch_size', 1: 'sequence_length'},
                'output': {0: 'batch_size', 1: 'sequence_length'}
            },
            verbose=True
        )
        print("Exported model!")

        # Verify export

        # Test with different sequence lengths
        test_lengths = [1, 6, 7, 16, 32, 64, 111]
        for test_length in test_lengths:
            test_input = torch.randn(1, test_length, C)
            test_mask = torch.ones(1, test_length)

            # Test with PyTorch model
            with torch.no_grad():
                torch_output = single_tmbed_model(test_input, test_mask)

            # Test with ONNX model
            ort_session = ort.InferenceSession(specific_onnx_file_path)
            ort_inputs = {
                'input': test_input.numpy(),
                'mask': test_mask.numpy()
            }
            ort_output = ort_session.run(None, ort_inputs)

            np.testing.assert_allclose(torch_output.numpy(), ort_output[0], rtol=1e-4, atol=1e-5)
            print(f"Test passed for sequence length {test_length}")

        print(f"Model has been successfully exported to {specific_onnx_file_path}")



export_tmbed_to_onnx()
