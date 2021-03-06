# Class `tensorflow::Tensor`

Represents an n-dimensional array of values.



##Member Summary

* [`tensorflow::Tensor::Tensor()`](#tensorflow_Tensor_Tensor)
  * Default Tensor constructor. Creates a 1-dimension, 0-element float tensor.
* [`tensorflow::Tensor::Tensor(DataType type, const TensorShape &shape)`](#tensorflow_Tensor_Tensor)
  * Creates a Tensor of the given `type` and `shape`.
* [`tensorflow::Tensor::Tensor(Allocator *a, DataType type, const TensorShape &shape)`](#tensorflow_Tensor_Tensor)
  * Creates a tensor with the input `type` and `shape`, using the allocator `a` to allocate the underlying buffer.
* [`tensorflow::Tensor::Tensor(DataType type)`](#tensorflow_Tensor_Tensor)
  * Creates an uninitialized Tensor of the given data type.
* [`tensorflow::Tensor::Tensor(const Tensor &other)`](#tensorflow_Tensor_Tensor)
* [`tensorflow::Tensor::~Tensor()`](#tensorflow_Tensor_Tensor)
  * Copy constructor.
* [`DataType tensorflow::Tensor::dtype() const`](#DataType_tensorflow_Tensor_dtype)
  * Returns the data type.
* [`const TensorShape& tensorflow::Tensor::shape() const`](#const_TensorShape_tensorflow_Tensor_shape)
  * Returns the shape of the tensor.
* [`int tensorflow::Tensor::dims() const`](#int_tensorflow_Tensor_dims)
  * Convenience accessor for the tensor shape.
* [`int64 tensorflow::Tensor::dim_size(int d) const`](#int64_tensorflow_Tensor_dim_size)
  * Convenience accessor for the tensor shape.
* [`int64 tensorflow::Tensor::NumElements() const`](#int64_tensorflow_Tensor_NumElements)
  * Convenience accessor for the tensor shape.
* [`bool tensorflow::Tensor::IsSameSize(const Tensor &b) const`](#bool_tensorflow_Tensor_IsSameSize)
* [`bool tensorflow::Tensor::IsInitialized() const`](#bool_tensorflow_Tensor_IsInitialized)
  * Has this Tensor been initialized?
* [`size_t tensorflow::Tensor::TotalBytes() const`](#size_t_tensorflow_Tensor_TotalBytes)
  * Returns the estimated memory usage of this tensor.
* [`Tensor& tensorflow::Tensor::operator=(const Tensor &other)`](#Tensor_tensorflow_Tensor_operator_)
  * Assign operator. This tensor shares other&apos;s underlying storage.
* [`bool tensorflow::Tensor::CopyFrom(const Tensor &other, const TensorShape &shape) TF_MUST_USE_RESULT`](#bool_tensorflow_Tensor_CopyFrom)
  * Copy the other tensor into this tensor and reshape it.
* [`Tensor tensorflow::Tensor::Slice(int64 dim0_start, int64 dim0_limit) const`](#Tensor_tensorflow_Tensor_Slice)
  * Slice this tensor along the 1st dimension.
* [`bool tensorflow::Tensor::FromProto(const TensorProto &other) TF_MUST_USE_RESULT`](#bool_tensorflow_Tensor_FromProto)
  * Parse `other` and construct the tensor.
* [`bool tensorflow::Tensor::FromProto(Allocator *a, const TensorProto &other) TF_MUST_USE_RESULT`](#bool_tensorflow_Tensor_FromProto)
* [`void tensorflow::Tensor::AsProtoField(TensorProto *proto) const`](#void_tensorflow_Tensor_AsProtoField)
  * Fills in `proto` with `*this` tensor&apos;s content.
* [`void tensorflow::Tensor::AsProtoTensorContent(TensorProto *proto) const`](#void_tensorflow_Tensor_AsProtoTensorContent)
* [`TTypes<T>::Vec tensorflow::Tensor::vec()`](#TTypes_T_Vec_tensorflow_Tensor_vec)
  * Return the tensor data as an `Eigen::Tensor` with the type and sizes of this ` Tensor `.
* [`TTypes<T>::Matrix tensorflow::Tensor::matrix()`](#TTypes_T_Matrix_tensorflow_Tensor_matrix)
* [`TTypes< T, NDIMS >::Tensor tensorflow::Tensor::tensor()`](#TTypes_T_NDIMS_Tensor_tensorflow_Tensor_tensor)
* [`TTypes<T>::Flat tensorflow::Tensor::flat()`](#TTypes_T_Flat_tensorflow_Tensor_flat)
  * Return the tensor data as an `Eigen::Tensor` of the data type and a specified shape.
* [`TTypes<T>::UnalignedFlat tensorflow::Tensor::unaligned_flat()`](#TTypes_T_UnalignedFlat_tensorflow_Tensor_unaligned_flat)
* [`TTypes<T>::Matrix tensorflow::Tensor::flat_inner_dims()`](#TTypes_T_Matrix_tensorflow_Tensor_flat_inner_dims)
* [`TTypes<T>::Matrix tensorflow::Tensor::flat_outer_dims()`](#TTypes_T_Matrix_tensorflow_Tensor_flat_outer_dims)
* [`TTypes< T, NDIMS >::Tensor tensorflow::Tensor::shaped(gtl::ArraySlice< int64 > new_sizes)`](#TTypes_T_NDIMS_Tensor_tensorflow_Tensor_shaped)
* [`TTypes< T, NDIMS >::UnalignedTensor tensorflow::Tensor::unaligned_shaped(gtl::ArraySlice< int64 > new_sizes)`](#TTypes_T_NDIMS_UnalignedTensor_tensorflow_Tensor_unaligned_shaped)
* [`TTypes< T >::Scalar tensorflow::Tensor::scalar()`](#TTypes_T_Scalar_tensorflow_Tensor_scalar)
  * Return the Tensor data as a `TensorMap` of fixed size 1: `TensorMap<TensorFixedSize<T, 1>>`.
* [`TTypes<T>::ConstVec tensorflow::Tensor::vec() const`](#TTypes_T_ConstVec_tensorflow_Tensor_vec)
  * Const versions of all the methods above.
* [`TTypes<T>::ConstMatrix tensorflow::Tensor::matrix() const`](#TTypes_T_ConstMatrix_tensorflow_Tensor_matrix)
* [`TTypes< T, NDIMS >::ConstTensor tensorflow::Tensor::tensor() const`](#TTypes_T_NDIMS_ConstTensor_tensorflow_Tensor_tensor)
* [`TTypes<T>::ConstFlat tensorflow::Tensor::flat() const`](#TTypes_T_ConstFlat_tensorflow_Tensor_flat)
* [`TTypes<T>::UnalignedConstFlat tensorflow::Tensor::unaligned_flat() const`](#TTypes_T_UnalignedConstFlat_tensorflow_Tensor_unaligned_flat)
* [`TTypes<T>::ConstMatrix tensorflow::Tensor::flat_inner_dims() const`](#TTypes_T_ConstMatrix_tensorflow_Tensor_flat_inner_dims)
* [`TTypes<T>::ConstMatrix tensorflow::Tensor::flat_outer_dims() const`](#TTypes_T_ConstMatrix_tensorflow_Tensor_flat_outer_dims)
* [`TTypes< T, NDIMS >::ConstTensor tensorflow::Tensor::shaped(gtl::ArraySlice< int64 > new_sizes) const`](#TTypes_T_NDIMS_ConstTensor_tensorflow_Tensor_shaped)
* [`TTypes< T, NDIMS >::UnalignedConstTensor tensorflow::Tensor::unaligned_shaped(gtl::ArraySlice< int64 > new_sizes) const`](#TTypes_T_NDIMS_UnalignedConstTensor_tensorflow_Tensor_unaligned_shaped)
* [`TTypes< T >::ConstScalar tensorflow::Tensor::scalar() const`](#TTypes_T_ConstScalar_tensorflow_Tensor_scalar)
* [`string tensorflow::Tensor::SummarizeValue(int64 max_entries) const`](#string_tensorflow_Tensor_SummarizeValue)
  * Render the first `max_entries` values in `*this` into a string.
* [`string tensorflow::Tensor::DebugString() const`](#string_tensorflow_Tensor_DebugString)
  * A human-readable summary of the tensor suitable for debugging.
* [`void tensorflow::Tensor::FillDescription(TensorDescription *description) const`](#void_tensorflow_Tensor_FillDescription)
* [`StringPiece tensorflow::Tensor::tensor_data() const`](#StringPiece_tensorflow_Tensor_tensor_data)
  * Returns a `StringPiece` mapping the current tensor&apos;s buffer.

##Member Details

#### [`tensorflow::Tensor::Tensor()`](#tensorflow_Tensor_Tensor) {#tensorflow_Tensor_Tensor}

Default Tensor constructor. Creates a 1-dimension, 0-element float tensor.



#### [`tensorflow::Tensor::Tensor(DataType type, const TensorShape &shape)`](#tensorflow_Tensor_Tensor) {#tensorflow_Tensor_Tensor}

Creates a Tensor of the given `type` and `shape`.

The underlying buffer is allocated using a `CPUAllocator`.

#### [`tensorflow::Tensor::Tensor(Allocator *a, DataType type, const TensorShape &shape)`](#tensorflow_Tensor_Tensor) {#tensorflow_Tensor_Tensor}

Creates a tensor with the input `type` and `shape`, using the allocator `a` to allocate the underlying buffer.

`a` must outlive the lifetime of this Tensor .

#### [`tensorflow::Tensor::Tensor(DataType type)`](#tensorflow_Tensor_Tensor) {#tensorflow_Tensor_Tensor}

Creates an uninitialized Tensor of the given data type.



#### [`tensorflow::Tensor::Tensor(const Tensor &other)`](#tensorflow_Tensor_Tensor) {#tensorflow_Tensor_Tensor}





#### [`tensorflow::Tensor::~Tensor()`](#tensorflow_Tensor_Tensor) {#tensorflow_Tensor_Tensor}

Copy constructor.



#### [`DataType tensorflow::Tensor::dtype() const`](#DataType_tensorflow_Tensor_dtype) {#DataType_tensorflow_Tensor_dtype}

Returns the data type.



#### [`const TensorShape& tensorflow::Tensor::shape() const`](#const_TensorShape_tensorflow_Tensor_shape) {#const_TensorShape_tensorflow_Tensor_shape}

Returns the shape of the tensor.



#### [`int tensorflow::Tensor::dims() const`](#int_tensorflow_Tensor_dims) {#int_tensorflow_Tensor_dims}

Convenience accessor for the tensor shape.

For all shape accessors, see comments for relevant methods of ` TensorShape ` in ` tensor_shape.h `.

#### [`int64 tensorflow::Tensor::dim_size(int d) const`](#int64_tensorflow_Tensor_dim_size) {#int64_tensorflow_Tensor_dim_size}

Convenience accessor for the tensor shape.



#### [`int64 tensorflow::Tensor::NumElements() const`](#int64_tensorflow_Tensor_NumElements) {#int64_tensorflow_Tensor_NumElements}

Convenience accessor for the tensor shape.



#### [`bool tensorflow::Tensor::IsSameSize(const Tensor &b) const`](#bool_tensorflow_Tensor_IsSameSize) {#bool_tensorflow_Tensor_IsSameSize}





#### [`bool tensorflow::Tensor::IsInitialized() const`](#bool_tensorflow_Tensor_IsInitialized) {#bool_tensorflow_Tensor_IsInitialized}

Has this Tensor been initialized?



#### [`size_t tensorflow::Tensor::TotalBytes() const`](#size_t_tensorflow_Tensor_TotalBytes) {#size_t_tensorflow_Tensor_TotalBytes}

Returns the estimated memory usage of this tensor.



#### [`Tensor& tensorflow::Tensor::operator=(const Tensor &other)`](#Tensor_tensorflow_Tensor_operator_) {#Tensor_tensorflow_Tensor_operator_}

Assign operator. This tensor shares other&apos;s underlying storage.



#### [`bool tensorflow::Tensor::CopyFrom(const Tensor &other, const TensorShape &shape) TF_MUST_USE_RESULT`](#bool_tensorflow_Tensor_CopyFrom) {#bool_tensorflow_Tensor_CopyFrom}

Copy the other tensor into this tensor and reshape it.

This tensor shares other&apos;s underlying storage. Returns `true` iff `other.shape()` has the same number of elements of the given `shape`.

#### [`Tensor tensorflow::Tensor::Slice(int64 dim0_start, int64 dim0_limit) const`](#Tensor_tensorflow_Tensor_Slice) {#Tensor_tensorflow_Tensor_Slice}

Slice this tensor along the 1st dimension.

I.e., the returned tensor satisfies returned[i, ...] == this[dim0_start + i, ...]. The returned tensor shares the underlying tensor buffer with this tensor.

NOTE: The returned tensor may not satisfies the same alignment requirement as this tensor depending on the shape. The caller must check the returned tensor&apos;s alignment before calling certain methods that have alignment requirement (e.g., ` flat() `, `tensor()`).

REQUIRES: ` dims() ` >= 1 REQUIRES: `0 <= dim0_start <= dim0_limit <= dim_size(0)`

#### [`bool tensorflow::Tensor::FromProto(const TensorProto &other) TF_MUST_USE_RESULT`](#bool_tensorflow_Tensor_FromProto) {#bool_tensorflow_Tensor_FromProto}

Parse `other` and construct the tensor.

Returns `true` iff the parsing succeeds. If the parsing fails, the state of `*this` is unchanged.

#### [`bool tensorflow::Tensor::FromProto(Allocator *a, const TensorProto &other) TF_MUST_USE_RESULT`](#bool_tensorflow_Tensor_FromProto) {#bool_tensorflow_Tensor_FromProto}





#### [`void tensorflow::Tensor::AsProtoField(TensorProto *proto) const`](#void_tensorflow_Tensor_AsProtoField) {#void_tensorflow_Tensor_AsProtoField}

Fills in `proto` with `*this` tensor&apos;s content.

` AsProtoField() ` fills in the repeated field for `proto.dtype()`, while `AsProtoTensorContent()` encodes the content in `proto.tensor_content()` in a compact form.

#### [`void tensorflow::Tensor::AsProtoTensorContent(TensorProto *proto) const`](#void_tensorflow_Tensor_AsProtoTensorContent) {#void_tensorflow_Tensor_AsProtoTensorContent}





#### [`TTypes<T>::Vec tensorflow::Tensor::vec()`](#TTypes_T_Vec_tensorflow_Tensor_vec) {#TTypes_T_Vec_tensorflow_Tensor_vec}

Return the tensor data as an `Eigen::Tensor` with the type and sizes of this ` Tensor `.

Use these methods when you know the data type and the number of dimensions of the Tensor and you want an `Eigen::Tensor` automatically sized to the ` Tensor ` sizes. The implementation check fails if either type or sizes mismatch.

Example:

```c++ typedef float T;
Tensor my_mat(...built with Shape{rows: 3, cols: 5}...);
auto mat = my_mat.matrix<T>();    // 2D Eigen::Tensor, 3 x 5.
auto mat = my_mat.tensor<T, 2>(); // 2D Eigen::Tensor, 3 x 5.
auto vec = my_mat.vec<T>();       // CHECK fails as my_mat is 2D.
auto vec = my_mat.tensor<T, 3>(); // CHECK fails as my_mat is 2D.
auto mat = my_mat.matrix<int32>();// CHECK fails as type mismatch.

```

#### [`TTypes<T>::Matrix tensorflow::Tensor::matrix()`](#TTypes_T_Matrix_tensorflow_Tensor_matrix) {#TTypes_T_Matrix_tensorflow_Tensor_matrix}





#### [`TTypes< T, NDIMS >::Tensor tensorflow::Tensor::tensor()`](#TTypes_T_NDIMS_Tensor_tensorflow_Tensor_tensor) {#TTypes_T_NDIMS_Tensor_tensorflow_Tensor_tensor}





#### [`TTypes<T>::Flat tensorflow::Tensor::flat()`](#TTypes_T_Flat_tensorflow_Tensor_flat) {#TTypes_T_Flat_tensorflow_Tensor_flat}

Return the tensor data as an `Eigen::Tensor` of the data type and a specified shape.

These methods allow you to access the data with the dimensions and sizes of your choice. You do not need to know the number of dimensions of the Tensor to call them. However, they `CHECK` that the type matches and the dimensions requested creates an `Eigen::Tensor` with the same number of elements as the tensor.

Example:

```c++ typedef float T;
Tensor my_ten(...built with Shape{planes: 4, rows: 3, cols: 5}...);
// 1D Eigen::Tensor, size 60:
auto flat = my_ten.flat<T>();
// 2D Eigen::Tensor 12 x 5:
auto inner = my_ten.flat_inner_dims<T>();
// 2D Eigen::Tensor 4 x 15:
auto outer = my_ten.shaped<T, 2>({4, 15});
// CHECK fails, bad num elements:
auto outer = my_ten.shaped<T, 2>({4, 8});
// 3D Eigen::Tensor 6 x 5 x 2:
auto weird = my_ten.shaped<T, 3>({6, 5, 2});
// CHECK fails, type mismatch:
auto bad   = my_ten.flat<int32>();

```

#### [`TTypes<T>::UnalignedFlat tensorflow::Tensor::unaligned_flat()`](#TTypes_T_UnalignedFlat_tensorflow_Tensor_unaligned_flat) {#TTypes_T_UnalignedFlat_tensorflow_Tensor_unaligned_flat}





#### [`TTypes<T>::Matrix tensorflow::Tensor::flat_inner_dims()`](#TTypes_T_Matrix_tensorflow_Tensor_flat_inner_dims) {#TTypes_T_Matrix_tensorflow_Tensor_flat_inner_dims}



Returns the data as an Eigen::Tensor with 2 dimensions, collapsing all Tensor dimensions but the last one into the first dimension of the result.

#### [`TTypes<T>::Matrix tensorflow::Tensor::flat_outer_dims()`](#TTypes_T_Matrix_tensorflow_Tensor_flat_outer_dims) {#TTypes_T_Matrix_tensorflow_Tensor_flat_outer_dims}



Returns the data as an Eigen::Tensor with 2 dimensions, collapsing all Tensor dimensions but the first one into the last dimension of the result.

#### [`TTypes< T, NDIMS >::Tensor tensorflow::Tensor::shaped(gtl::ArraySlice< int64 > new_sizes)`](#TTypes_T_NDIMS_Tensor_tensorflow_Tensor_shaped) {#TTypes_T_NDIMS_Tensor_tensorflow_Tensor_shaped}





#### [`TTypes< T, NDIMS >::UnalignedTensor tensorflow::Tensor::unaligned_shaped(gtl::ArraySlice< int64 > new_sizes)`](#TTypes_T_NDIMS_UnalignedTensor_tensorflow_Tensor_unaligned_shaped) {#TTypes_T_NDIMS_UnalignedTensor_tensorflow_Tensor_unaligned_shaped}





#### [`TTypes< T >::Scalar tensorflow::Tensor::scalar()`](#TTypes_T_Scalar_tensorflow_Tensor_scalar) {#TTypes_T_Scalar_tensorflow_Tensor_scalar}

Return the Tensor data as a `TensorMap` of fixed size 1: `TensorMap<TensorFixedSize<T, 1>>`.

Using ` scalar() ` allows the compiler to perform optimizations as the size of the tensor is known at compile time.

#### [`TTypes<T>::ConstVec tensorflow::Tensor::vec() const`](#TTypes_T_ConstVec_tensorflow_Tensor_vec) {#TTypes_T_ConstVec_tensorflow_Tensor_vec}

Const versions of all the methods above.



#### [`TTypes<T>::ConstMatrix tensorflow::Tensor::matrix() const`](#TTypes_T_ConstMatrix_tensorflow_Tensor_matrix) {#TTypes_T_ConstMatrix_tensorflow_Tensor_matrix}





#### [`TTypes< T, NDIMS >::ConstTensor tensorflow::Tensor::tensor() const`](#TTypes_T_NDIMS_ConstTensor_tensorflow_Tensor_tensor) {#TTypes_T_NDIMS_ConstTensor_tensorflow_Tensor_tensor}





#### [`TTypes<T>::ConstFlat tensorflow::Tensor::flat() const`](#TTypes_T_ConstFlat_tensorflow_Tensor_flat) {#TTypes_T_ConstFlat_tensorflow_Tensor_flat}





#### [`TTypes<T>::UnalignedConstFlat tensorflow::Tensor::unaligned_flat() const`](#TTypes_T_UnalignedConstFlat_tensorflow_Tensor_unaligned_flat) {#TTypes_T_UnalignedConstFlat_tensorflow_Tensor_unaligned_flat}





#### [`TTypes<T>::ConstMatrix tensorflow::Tensor::flat_inner_dims() const`](#TTypes_T_ConstMatrix_tensorflow_Tensor_flat_inner_dims) {#TTypes_T_ConstMatrix_tensorflow_Tensor_flat_inner_dims}





#### [`TTypes<T>::ConstMatrix tensorflow::Tensor::flat_outer_dims() const`](#TTypes_T_ConstMatrix_tensorflow_Tensor_flat_outer_dims) {#TTypes_T_ConstMatrix_tensorflow_Tensor_flat_outer_dims}





#### [`TTypes< T, NDIMS >::ConstTensor tensorflow::Tensor::shaped(gtl::ArraySlice< int64 > new_sizes) const`](#TTypes_T_NDIMS_ConstTensor_tensorflow_Tensor_shaped) {#TTypes_T_NDIMS_ConstTensor_tensorflow_Tensor_shaped}





#### [`TTypes< T, NDIMS >::UnalignedConstTensor tensorflow::Tensor::unaligned_shaped(gtl::ArraySlice< int64 > new_sizes) const`](#TTypes_T_NDIMS_UnalignedConstTensor_tensorflow_Tensor_unaligned_shaped) {#TTypes_T_NDIMS_UnalignedConstTensor_tensorflow_Tensor_unaligned_shaped}





#### [`TTypes< T >::ConstScalar tensorflow::Tensor::scalar() const`](#TTypes_T_ConstScalar_tensorflow_Tensor_scalar) {#TTypes_T_ConstScalar_tensorflow_Tensor_scalar}





#### [`string tensorflow::Tensor::SummarizeValue(int64 max_entries) const`](#string_tensorflow_Tensor_SummarizeValue) {#string_tensorflow_Tensor_SummarizeValue}

Render the first `max_entries` values in `*this` into a string.



#### [`string tensorflow::Tensor::DebugString() const`](#string_tensorflow_Tensor_DebugString) {#string_tensorflow_Tensor_DebugString}

A human-readable summary of the tensor suitable for debugging.



#### [`void tensorflow::Tensor::FillDescription(TensorDescription *description) const`](#void_tensorflow_Tensor_FillDescription) {#void_tensorflow_Tensor_FillDescription}



Fill in the `TensorDescription` proto with metadata about the tensor that is useful for monitoring and debugging.

#### [`StringPiece tensorflow::Tensor::tensor_data() const`](#StringPiece_tensorflow_Tensor_tensor_data) {#StringPiece_tensorflow_Tensor_tensor_data}

Returns a `StringPiece` mapping the current tensor&apos;s buffer.

The returned `StringPiece` may point to memory location on devices that the CPU cannot address directly.

NOTE: The underlying tensor buffer is refcounted, so the lifetime of the contents mapped by the `StringPiece` matches the lifetime of the buffer; callers should arrange to make sure the buffer does not get destroyed while the `StringPiece` is still used.

REQUIRES: `DataTypeCanUseMemcpy( dtype() )`.
