from pyhocon import ConfigFactory

# Example config string (trimmed for brevity)
conf_text = """
{
    general {
        base_exp_dir = ./exp/data_BlendedMVS/bmvs_bear/womask_sphere
    }
    model {
        sdf_network {
            d_out : 257,
            d_in : 3,
            d_hidden : 256
        }
    }
}
"""
if __name__ == '__main__':
    # Replace placeholder if necessary
    conf_text = conf_text.replace('CASE_NAME', 'bear')

    # Parse the configuration
    conf = ConfigFactory.parse_string(conf_text)

    # Access and print configuration to verify types and values
    print('d_out:', conf['model']['sdf_network']['d_out'])  # Should output: d_out: 257
    print('d_in:', conf['model']['sdf_network']['d_in'])    # Should output: d_in: 3
    print('d_hidden:', conf['model']['sdf_network']['d_hidden'])  # Should output: d_hidden: 256
